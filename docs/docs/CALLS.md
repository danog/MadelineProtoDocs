---
title: "Telegram voice/video/group calls"
description: "MadelineProto can make and receive voice and video calls, stream and record video chats and livestreams, and take part in end-to-end encrypted conference calls."
nav_order: 21
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Telegram voice/video/group calls

MadelineProto can make and receive voice and video calls, stream and record video chats and livestreams, and take part in end-to-end encrypted conference calls.

The whole call stack (WebRTC, the Telegram signaling protocols and the media demuxers) is written in pure PHP, so calls work everywhere MadelineProto works, webhosts included, without any extension or external program.

[Full video webradio example](https://github.com/danog/magnaluna): try it live on Telegram, [@magicalcrazypony](https://t.me/magicalcrazypony)!

* [Call types](#call-types)
* [Requesting a call](#requesting-a-call)
* [Accepting calls](#accepting-calls)
* [Playing video files](#playing-video-files)
* [Playing audio files](#playing-audio-files)
* [Supported formats](#supported-formats)
* [Playlists and screen sharing](#playlists-and-screen-sharing)
* [Recording calls](#recording-calls)
* [Group calls (video chats and livestreams)](#group-calls-video-chats-and-livestreams)
  * [Livestreams, RTMP and stream mode](#livestreams-rtmp-and-stream-mode)
  * [Live stories](#live-stories)
  * [Streaming to a profile or livestream from its RTMP URL](#streaming-to-a-profile-or-livestream-from-its-rtmp-url)
* [Conference calls](#conference-calls)
* [Restarts](#restarts)

## Call types

Every call implements the [Call](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Call.html) interface, so the same code can play files into and record any kind of call:

* [PrivateCall](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Calls/PrivateCall.html): a one-to-one voice or video call (`danog\MadelineProto\VoIP` is an alias kept for backwards compatibility).
* [GroupCall](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Calls/GroupCall.html): a video chat or livestream of a group or channel.
* [LiveStory](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Calls/LiveStory.html): a livestream posted as a story.
* [ConferenceCall](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Calls/ConferenceCall.html): an end-to-end encrypted multi-party call.

The multi-party ones also implement the [MultiCall](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/MultiCall.html) interface, which adds participant management and in-call messages.

## Requesting a call

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// A voice call...
$call = $MadelineProto->requestCall('@danogentili');
// ...or a video call.
$call = $MadelineProto->requestCall('@danogentili', video: true);
```

The [requestCall](https://docs.madelineproto.xyz/requestCall.html) function accepts the ID/username/Peer/User/InputPeer of the person to call, and returns a [PrivateCall](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Calls/PrivateCall.html) object, used to play files, record the call, mute ourselves and hang up with `discard()`.

Calls can only be made by users, not by bots.

From an event handler, messages can start calls directly: in a private chat, `requestCall()` returns the call already running with the other user, or calls them. `canRequestCall()` and `getCallDenialReason()` tell beforehand whether that will work, and why not (the user's privacy settings may not allow it, video calls may be unavailable for the other user...):

```php
use danog\MadelineProto\EventHandler\Filter\FilterCommand;
use danog\MadelineProto\EventHandler\Message\PrivateMessage;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\RemoteUrl;

#[FilterCommand('call')]
public function callCommand(Incoming&PrivateMessage $message): void
{
    if ($reason = $message->getCallDenialReason(video: true)) {
        $message->reply("Can't call you: {$reason->value}");
        return;
    }
    $message->requestCall(video: true)->play(new RemoteUrl('https://paste.daniil.it/oncall.webm'));
}
```

In a group or channel, `requestCall()` returns the active video chat instead, or creates one (which requires the `manage_call` admin right): video chats are not joined automatically, so call `join()` on it before playing anything. `$message->requestCall()->join()` works in every chat, since joining an outgoing one-to-one call does nothing.

`requestCall()` throws a `CallNotAllowedException` (whose `reason` is a `CallDenialReason`) when the call can't be made.

## Accepting calls

Incoming calls arrive in the event handler as `PrivateCall` updates: accept them with `join()`.

```php
<?php

declare(strict_types=1);

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\EventHandler\Attributes\Handler;
use danog\MadelineProto\EventHandler\Calls\PrivateCall;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\RemoteUrl;

class PonyHandler extends \danog\MadelineProto\SimpleEventHandler
{
    #[Handler]
    public function handleIncomingCall(PrivateCall&Incoming $call): void
    {
        $call->join()->play(new RemoteUrl('https://paste.daniil.it/oncall.webm'));
    }
}

PonyHandler::startAndLoop('session.madeline');
```

`$call->video` tells whether the other party started a video call, and `getVisualization()` returns the four key verification emojis, which both parties can compare to make sure nobody is listening in.

## Playing video files

Playing a WebM or Matroska file with a video track transmits its video along with its audio, in every kind of call:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\LocalFile;
use danog\MadelineProto\RemoteUrl;

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili', video: true);
$call->play(new RemoteUrl('https://paste.daniil.it/oncall.webm'))
     ->then(new LocalFile('video.mkv'));
```

The video frames are sent exactly as they are stored in the file: nothing is decoded or re-encoded, so playing video needs no codec library, and costs about as much CPU as playing audio.

In a one-to-one call, video is turned on as soon as a file with video starts playing (even in a call started as a voice call), and off when a file without video follows it. Only one video is transmitted at a time in a one-to-one call: while the screen is being shared (see [screen sharing](#playlists-and-screen-sharing)), the camera stream pauses.

See [supported formats](#supported-formats) for the video codecs that can be played.

## Playing audio files

Audio files are played the same way:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\LocalFile;
use danog\MadelineProto\RemoteUrl;

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili');
$call->play(new LocalFile('audio.webm'))     // WebM/Matroska with OPUS audio
     ->then(new LocalFile('audio.ogg'))      // OGG OPUS
     ->then(new RemoteUrl('https://example.com/audio.webm'));
```

Telegram files can be played as streams too, with no need to download them first:

```php
use danog\MadelineProto\EventHandler\Attributes\Handler;
use danog\MadelineProto\EventHandler\Media\Document;
use danog\MadelineProto\EventHandler\Message\PrivateMessage;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;

// Plays the WebM and OGG files we receive into a call with the sender.
#[Handler]
public function playFile(Incoming&PrivateMessage $message): void
{
    if ($message->media instanceof Document
        && in_array($message->media->mimeType, ['audio/ogg', 'video/webm'], true)
        && $message->canRequestCall()
    ) {
        $message->requestCall()->play($message->media->getStream());
    }
}
```

## Supported formats

MadelineProto plays these formats on its own, without ffmpeg or any extension:

* **WebM and Matroska** (`.webm`, `.mkv`) files, with:
  * **VP8**, **VP9**, **H.264** or **H.265** video (**AV1** can also be used in one-to-one calls, if the other party's app supports it);
  * **OPUS** audio.
  
  Files may hold video and audio, video only or audio only. Other audio codecs (Vorbis, AAC...) are skipped with a warning, as are video tracks after the first one.
* **OGG OPUS** (`.ogg`, `.opus`) files, mono or stereo, with any frame size.

Files in these formats can be local files, URLs or streams.

YouTube videos (h264, h265, VP8, VP9 inside .webm, .mkv) can also be sent as-is, without re-encoding (including in streaming mode).

Other formats (MP3, FLAC, WAV, MP4...) can only be played if the FFI extension, libopus and ffmpeg are installed on the server, in which case their audio is converted on the fly (any video is dropped).

## Playlists and screen sharing

Every call has a playlist:

```php
use danog\MadelineProto\LocalFile;
use danog\MadelineProto\MediaDestination;

$call->play(new LocalFile('first.webm'));  // Starts playing now (or after the current file).
$call->then(new LocalFile('second.webm')); // Queued after it.

// Played on loop while the playlist is empty.
$call->playOnHold(MediaDestination::Camera, new LocalFile('hold.webm'));

$call->pause();
$call->resume();
$call->skip();          // Skips to the next file.
$call->stop();          // Clears the playlist and the hold files.
$call->getCurrent();    // The file being played.
$call->setMuted(true);  // Mutes our own audio.

// Plays a video as a screen share, next to the camera stream.
$call->play(new LocalFile('slides.webm'), MediaDestination::Presentation);
$call->disablePresentation(); // Stops sharing the screen.
```

Every playlist method takes a `MediaDestination`: `Camera` (the default) for the main audio and video stream, or `Presentation` for the screen share, which is started by the first file played into it, and transmits only the video of its files.

`playBlocking()` works like `play()`, but if a stream was passed, it waits until it has been played.

Files are read just ahead of playback, to keep memory usage to a minimum, which matters when playing in many calls at once on webhosts with little RAM. When playing from slow sources (like slow URLs), you can read further ahead with `$settings->getVoip()->setPlaybackLookahead($milliseconds)`, at the cost of the file's bitrate times the lookahead of memory per call (between 0.5 and 2 MB per call for a 2-second lookahead on a 2 Mbps video, depending on the part being played).

## Recording calls

To record the incoming media of a call, use `setOutput` (one file with a fixed set of tracks) or `setOutputFolder` (a directory, one file per combination of streams):

```php
<?php

declare(strict_types=1);

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\CallStream;
use danog\MadelineProto\EventHandler\Attributes\Handler;
use danog\MadelineProto\EventHandler\Calls\CallStreams;
use danog\MadelineProto\EventHandler\Calls\PrivateCall;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\LocalDirectory;
use danog\MadelineProto\LocalFile;
use danog\MadelineProto\RemoteUrl;

class PonyHandler extends \danog\MadelineProto\SimpleEventHandler
{
    #[Handler]
    public function handleIncomingCall(PrivateCall&Incoming $call): void
    {
        $call->join();
        $call->play(new RemoteUrl('https://paste.daniil.it/oncall.webm'));

        // Records the incoming audio as an OGG OPUS stream: a .mkv or .webm name records video too.
        $call->setOutput(new LocalFile('output.ogg'));

        // Records every stream the other party is sending right now (mic, camera, screen share)
        // into one Matroska file, and returns them as a bitmask of CallStream flags.
        $streams = $call->setOutput(new LocalFile('call.mkv'));

        // Records only the audio and the screen share: every chosen stream must be available,
        // or an exception is thrown.
        $call->setOutput(new LocalFile('screen.mkv'), streams: CallStream::AUDIO | CallStream::SCREEN);

        // Records into a directory instead: a new numbered file (0_audio.mkv, 1_audio,video.mkv, …)
        // every time the other party turns a stream on or off.
        $call->setOutputFolder(new LocalDirectory('recordings'));

        // $stream can also be a WritableStream.
        // Can be used to pipe OGG OPUS or WebM data to ffmpeg, asterisk via amphp/process, amphp/socket, etc...
        //
        //$call->setOutput($stream);
    }

    // Emitted for every call type, whenever the streams a participant sends (or their codecs)
    // change, and whenever a recording ends.
    #[Handler]
    public function onStreams(CallStreams $update): void
    {
        $this->logger("Participant {$update->participant} of {$update->call} sends ".CallStream::describe($update->streams).': '.json_encode($update->codecs));
        if ($update->recordingStopped) {
            $this->logger("The recording of {$update->participant} ended");
        } elseif ($update->has(CallStream::VIDEO)) {
            // The camera is on: a file opened before it came on keeps its tracks, so start a new
            // one holding it (finishing the previous one).
            $update->call->setOutput(new LocalFile('call_video.mkv'), $update->participant, streams: CallStream::AUDIO | CallStream::VIDEO);
        }
    }
}

PonyHandler::startAndLoop('session.madeline');
```

Recordings are written in pure PHP, without decoding anything: the video tracks keep the codec the participant sends (VP8, VP9, H.264, H.265 or AV1), and the audio is OPUS.

A file recorded with `setOutput` keeps its tracks for its whole duration: a stream the participant turns off simply stops being written and resumes when it comes back, and a stream that becomes available later is not added (call `setOutput` again to start a new file with it). Only a change of codec of a video stream, or the end of the call, finishes the file early. A `setOutputFolder` recording follows every change instead, closing the current file and opening a new one named after the streams it holds (`<n>_<streams>.mkv`, with `streams` listing `audio`, `video` and `screen`).

In multi-party calls, `setOutput` records one participant, passed as second parameter, while `setOutputFolder` records every participant that sends something to its own series of files (or just one, if passed). Our own media is never recorded.

## Group calls (video chats and livestreams)

Group calls are handled through the `GroupCall` object, which implements the `MultiCall` interface (a superset of the `Call` interface used above: the same playlist, mute, screen-share and recording controls, plus multi-party management). What a video chat shares with a live story lives in their common base class, `AbstractGroupCall`; what only a video chat offers (scheduling, server-side recording, raising a hand) lives on `GroupCall` itself.

```php
use danog\MadelineProto\CallStream;
use danog\MadelineProto\LocalDirectory;
use danog\MadelineProto\LocalFile;
use danog\MadelineProto\MediaDestination;
use danog\MadelineProto\ParseMode;
use danog\MadelineProto\RemoteUrl;

// Create a video chat in a group or channel we administer (or a scheduled one, or an RTMP livestream), and join it...
$call = $this->createGroupCall('@mygroup', title: 'Weekly meeting')->join();
// ...or join the one currently active there, optionally as one of our channels.
$call = $this->joinGroupCall('@mygroup', muted: false, joinAs: '@mychannel');

// Playback and recording work exactly like in one-to-one calls.
$call->play(new LocalFile('video.webm'));                                   // camera and microphone
$call->play(new LocalFile('slides.webm'), MediaDestination::Presentation); // screen share
$call->setOutputFolder(new LocalDirectory('recordings'));                  // one numbered .mkv series per participant
$call->setOutput(new LocalFile('bob.mkv'), '@bob');                        // a single participant, one file with fixed tracks
$call->setOutput(new LocalFile('bob_audio.mkv'), '@bob', streams: CallStream::AUDIO);

// Manage the call (admin operations require the right admin rights).
$call->setTitle('New title');
$call->invite('@alice', '@bob');
$link = $call->exportInvite(canSelfUnmute: true);
$call->muteParticipant('@bob');
$call->setParticipantVolume('@alice', 15000);
$call->raiseHand();
$call->setJoinMuted(true);
$call->startRecording('Meeting', video: true);
$call->removeParticipant('@spammer');

// In-call messages and reactions, shown as an overlay by the participants' clients.
$call->setMessagesEnabled(true);
$call->sendMessage('**Hello everyone!**', ParseMode::MARKDOWN);
$call->sendReaction('👍');

// Participants.
foreach ($call->getParticipants() as $peerId => $participant) {
    echo "$peerId: muted={$participant->muted}, video={$participant->videoJoined}\n";
}

$call->leave();   // leave, keeping the call running
$call->discard(); // end the call for everyone
```

Group calls and conference calls carry VP8, VP9, H.264 and H.265 video.

Scheduled calls can be started early with `startScheduled()`, and `setStartSubscription(true)` asks for a notification when they start. `getGroupCallJoinAs($peer)` lists the peers we may join a call as, and `saveDefaultGroupCallJoinAs($peer, $joinAs)` stores the default.

Your event handler receives a `GroupCall` update whenever a call starts, changes or ends, a `GroupCallParticipants` update when participants join, leave or change state, a `GroupCallMessage` update for every in-call message or reaction (`LiveStoryMessage` and `ConferenceCallMessage` for live stories and conference calls), and a `GroupCallMessagesDeleted` update when messages are deleted:

```php
use danog\MadelineProto\EventHandler\Attributes\Handler;
use danog\MadelineProto\EventHandler\Calls\GroupCallMessage;

#[Handler]
public function onCallMessage(GroupCallMessage $message): void
{
    echo "{$message->fromId}: {$message->message->text}\n";
}
```

### Livestreams, RTMP and stream mode

Large livestreams (and every RTMP livestream) are received in [stream mode](https://core.telegram.org/api/group-calls#stream-mode): the server serves the mixed media as downloadable chunks rather than over WebRTC. `isStreamMode()` tells whether a call is in stream mode; nothing can be transmitted in it (except by publishing to an RTMP livestream, see below), but it can be recorded with `setOutput()` without specifying a participant: an RTMP livestream's audio and video into a `.mkv`/`.webm` file (or its audio into a `.ogg`), and an automatically-scaled livestream's mixed audio into any format. Recording into a directory with `setOutputFolder()` writes the mixed stream to `stream.mkv` (or `.ogg`) and additionally each publisher's video of an automatically-scaled livestream to `video-<endpoint>.mkv`. The MP4 segments the server uses are demuxed in pure PHP by the `Mp4` class, which can also be used on its own.

To publish an RTMP livestream, create the call with `createGroupCall($peer, rtmpStream: true)` in a group or channel we administer, and `play()` (or `playOnHold()`) files into it, just like into a video chat: MadelineProto publishes them over RTMP itself, while joining the call only watches it (so it can also be recorded as above). An RTMP livestream only carries H.264 video and AAC audio, in MP4 (with its `moov` at the start) or Matroska files, played as they are, without transcoding: convert other files first, e.g. with `ffmpeg -i input -c:v libx264 -c:a aac -movflags +faststart output.mp4`. Telegram scales every RTMP livestream to 1280x720 without keeping the aspect ratio, so pad other aspect ratios to 16:9 first (e.g. with `-vf 'scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2'`). To publish with another RTMP tool (OBS, ffmpeg...) instead, get the RTMP URL and stream key with `getGroupCallStreamRtmpUrl($peer)`.

### Live stories

A [live story](https://core.telegram.org/api/group-calls#live-stories) is a livestream posted as a story, of which we are the only publisher: `startLive($peer, caption: 'Hi!')` starts one and returns a `LiveStory`, which is used like any other group call (`play()` to stream, `sendMessage()` and `sendReaction()` to comment) and arrives in event handlers as a `LiveStory` update. Viewers may donate Telegram Stars: `setPaidMessagesStars($stars)` sets the minimum donation required to comment, `donate($stars)` donates, and `getStars()` returns the donations received so far and the top donors.

To stream to the profile of the account MadelineProto is logged in as, start a live story as `'me'`. With `rtmpStream: true`, what is played is published over RTMP, as to an RTMP livestream (H.264 video and AAC audio, see above): MadelineProto gets the stream key of the live story itself, and the live story doesn't even need to be joined. Otherwise, join it and play files as in a video chat.

```php
use danog\MadelineProto\RemoteUrl;

// Over RTMP: H.264 + AAC files (MP4 or Matroska).
$live = $MadelineProto->startLive('me', caption: 'Live from MadelineProto!', rtmpStream: true);
$live->play(new RemoteUrl('https://example.com/video.mp4'));

// Or over WebRTC, like a video chat (WebM/OGG files, or anything ffmpeg can convert).
$live = $MadelineProto->startLive('me');
$live->join();
$live->play(new RemoteUrl('https://example.com/video.webm'));

// End it.
$live->discard();
```

### Streaming to a profile or livestream from its RTMP URL

The Telegram apps can start a live story on a user's profile, or an RTMP livestream in a group or channel, "with another app": they show an RTMP server URL and a stream key, for encoders like OBS or ffmpeg. MadelineProto can be that encoder for anyone who gives it the URL and key, without being an admin or joining anything: `startRtmpStream()` returns an `RtmpStream`, with the playlist controls of a call (`play()`, `then()`, `playOnHold()`, `skip()`, `stop()`, `pause()`, `resume()`, `getCurrent()`; they're the methods of the `MediaPlayer` interface, which every call implements too).

```php
use danog\MadelineProto\LocalFile;
use danog\MadelineProto\MediaDestination;
use danog\MadelineProto\RemoteUrl;
use danog\MadelineProto\RtmpServers;

// The server URL followed by the stream key, as copied from the app (or startRtmpStream($url, $key)).
$stream = $MadelineProto->startRtmpStream('rtmps://dc4-1.rtmp.t.me/s/123456:AbCdEf', servers: RtmpServers::Telegram);

$stream->playOnHold(MediaDestination::Camera, new LocalFile('loop.mp4')); // Looped while the playlist is empty
$stream->play(new RemoteUrl('https://example.com/video.mp4'));
$stream->skip();

// Stop streaming for good.
$stream->close();
```

As in RTMP livestreams, only H.264 video and AAC audio can be streamed, in MP4 or Matroska files. MadelineProto connects when the stream is started, waits for the connection before playing (so that the first frames, and with them the first keyframe, aren't lost), and reconnects if the connection drops. The stream keeps going, across restarts too, until it's closed: `getRtmpStreams()` lists the streams, `getRtmpStream($url)` finds the one to a URL and key, and starting a stream to the same URL and key again returns the same one.

When the URL comes from someone else (the users of a bot, say), restrict where MadelineProto may connect with `servers`, so that it can't be pointed into your own network:

* `RtmpServers::Telegram`: only Telegram's RTMP servers (`*.rtmp.t.me`).
* `RtmpServers::Internet`: only servers on the internet: every address the server's name resolves to must be global (no loopback, private, link-local, shared or reserved address).
* `RtmpServers::Any`: any server (the default).

The check is made both when the stream starts (`startRtmpStream()` throws an `RtmpAddressException`) and at each connection, connecting to the address that was checked: a stream whose server is refused later is closed.

## Conference calls

[Conference calls](https://core.telegram.org/api/group-calls#conference-calls) are end-to-end encrypted multi-party calls not associated with any group, handled through the `ConferenceCall` object, which implements the same `MultiCall` interface (their encryption is implemented in pure PHP too, and uses the `sodium` and `openssl` extensions if available, for speed):

```php
// Create one (we are its only participant until someone joins)...
$call = $this->createConferenceCall();
$link = $call->exportInvite();          // https://t.me/call/... link anyone can join with
$call->invite('@alice');                 // or ring someone directly

// ...or join one from a link, or from an invitation service message.
$call = $this->joinConferenceCallBySlug('abcdef');
$call = $this->joinConferenceCallByInviteMessage($msgId);

$call->play(new LocalFile('video.webm'));                  // end-to-end encrypted audio and video
$call->setOutputFolder(new LocalDirectory('recordings')); // decrypted, one numbered .mkv series per participant
$call->setOutput(new LocalFile('alice.mkv'), '@alice');    // decrypted, a single participant

// The key verification emojis, which every participant must compare.
$emojis = $call->getVisualization();

$call->sendMessage('Hi!');               // end-to-end encrypted in-call message
$call->removeParticipant('@intruder');   // rekeys, so they cannot decrypt anything any more
$call->leave();
```

Invitations arrive as `DialogConferenceCall` service messages, which can be accepted with `join()` or declined with `decline()`. A one-to-one call can be upgraded to a conference with `migrateCallToConference($callId)`.

## Restarts

Calls survive restarts of MadelineProto: the calls we are in, their playlists and their recordings are saved in the session, and so are the RTMP streams (see above), which reconnect after a restart.

After a restart, the WebM or OGG file that was playing continues where it left off, the rest of the playlist and the hold files are played after it, and recordings continue in the same file. Files, URLs and resumable streams (such as the ones returned by `getStream()` on Telegram media) survive restarts; other streams can't be saved in the session.

When MadelineProto is used through its IPC server (i.e. not from an event handler), files, URLs and resumable streams are passed to the call by value; other streams are read from the client process, so `play()` blocks until they have been played. Files played on hold must be files, URLs or resumable streams.

<a href="https://docs.madelineproto.xyz/docs/FILES.html">Next section</a>