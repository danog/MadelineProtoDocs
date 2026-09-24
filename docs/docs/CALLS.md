---
title: "Telegram VoIP phone calls"
description: "MadelineProto provides an easy wrapper to work with phone calls."
nav_order: 21
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Telegram VoIP phone calls

MadelineProto provides an easy wrapper to work with phone calls.

[Full webradio example](https://github.com/danog/magnaluna)

* Please read the whole [VoIP API documentation](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html) before proceeding.
* [Requesting a call](#requesting-a-call)
* [Playing audio files](#playing-audio-files)
  * [Webhost support!](#webhost-support)
* [Accepting calls](#accepting-calls)


## Requesting a call
```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili');
```

The [requestCall](https://docs.madelineproto.xyz/requestCall.html) function accepts one parameter with the ID/username/Peer/User/InputPeer of the person to call, and returns a VoIP object that can be used to play audio files, set the hold files, change the configuration and set the output file (see the [VoIP API documentation](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html) for more info).

You can play audio files of any format as follows:

## Playing audio files

To play audio files of any format, install `ffmpeg`, `libopus` and enable the PHP `ffi` extension.  

If you can't do the above (for example on webhosts), **no problem**: simply pre-convert the files to a special format using [@libtgvoipbot, see here &raquo;](#webhost-support) for more info.  

You can play audio files:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\LocalFile;

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili');
$call->play(new LocalFile("audio.mp3"))
     ->then(new LocalFile("audio.flac"))
     ->then(new LocalFile("audio.wav"))
     ->then(new LocalFile("audio_with_video.mp4"));
```

You can also play remote streams (or simple remote files) by URL:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\RemoteUrl;

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili');
$call->play(new RemoteUrl("http://icestreaming.rai.it/1.mp3"));
```

You can also play Telegram files, using AMP streams!


## Webhost support

Starting from MadelineProto 8, VoIP now works on webhosts, too, thanks to a pure PHP implementation of libtgvoip and a pure PHP OGG demuxer!

The only limitation when running on webhosts is that audio files must be preconverted using by sending them to [@libtgvoip_bot](https://t.me/libtgvoip_bot) ([source code](https://github.com/danog/MadelineProto/blob/v8/examples/libtgvoipbot.php)), or by using the following script on your PC:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\LocalFile;

\danog\MadelineProto\Ogg::convert(new LocalFile("in.mp3"), new LocalFile("out.ogg"));
```

Copy out.ogg to your webhost, and then run this script on your webhost:

```php
<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\LocalFile;

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$call = $MadelineProto->requestCall('@danogentili');
$call->play(new LocalFile("out.ogg"));
```

## Accepting calls

Accepting calls is just as easy:

```php
<?php

declare(strict_types=1);

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\VoIP;
use danog\MadelineProto\RemoteUrl;
use danog\MadelineProto\EventHandler\Attributes\Handler;

class PonyHandler extends \danog\MadelineProto\SimpleEventHandler
{
    #[Handler]
    public function handleIncomingCall(VoIP&Incoming $call): void
    {
        $call->join()->play(new RemoteUrl('http://icestreaming.rai.it/1.mp3'));
    }
}

PonyHandler::startAndLoop('session.madeline');
```

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
use danog\MadelineProto\EventHandler\Calls\CallStreams;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\VoIP;
use danog\MadelineProto\RemoteUrl;
use danog\MadelineProto\LocalDirectory;
use danog\MadelineProto\LocalFile;
use danog\MadelineProto\RecordingEvent;
use danog\MadelineProto\EventHandler\Attributes\Handler;
use Amp\ByteStream\WritableStream;

class PonyHandler extends \danog\MadelineProto\SimpleEventHandler
{
    #[Handler]
    public function handleIncomingCall(VoIP&Incoming $call): void
    {
        $call->join();
        $call->play(new RemoteUrl('http://icestreaming.rai.it/1.mp3'));

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
    // change, and whenever a recording starts or ends.
    #[Handler]
    public function onStreams(CallStreams $update): void
    {
        $this->logger("Participant {$update->participant} of {$update->call} sends ".CallStream::describe($update->streams).': '.json_encode($update->codecs));
        if ($update->recording === RecordingEvent::Started) {
            $this->logger("Recording {$update->file?->file} started");
        } elseif ($update->recording === RecordingEvent::Ended) {
            $this->logger("Recording {$update->file?->file} ended");
        } elseif ($update->has(CallStream::VIDEO)) {
            // The camera is on: a file opened before it came on keeps its tracks, so start a new
            // one holding it (finishing the previous one).
            $update->call->setOutput(new LocalFile('call_video.mkv'), $update->participant, streams: CallStream::AUDIO | CallStream::VIDEO);
        }
    }

    // Plays incoming audio files into a Telegram call
    #[Handler]
    public function playAudio(Incoming&PrivateMessage&HasAudio $message): void
    {
        $this->requestCall($message->senderId)->play($message->media->getStream());
    }
}

PonyHandler::startAndLoop('session.madeline');
```

A file recorded with `setOutput` keeps its tracks for its whole duration: a stream the participant turns off simply stops being written and resumes when it comes back, and a stream that becomes available later is not added (call `setOutput` again to start a new file with it). Only a change of codec of a video stream, or the end of the call, finishes the file early. A `setOutputFolder` recording follows every change instead, closing the current file and opening a new one named after the streams it holds (`<n>_<streams>.mkv`, with `streams` listing `audio`, `video` and `screen`).

<a href="https://docs.madelineproto.xyz/docs/FILES.html">Next section</a>

## Group calls (video chats and livestreams)

Group calls are handled through the `GroupCall` object, which implements the `MultiCall` interface (a superset of the one-to-one `Call` interface used above: the same playlist, mute, screen-share and recording controls, plus multi-party management). What a video chat shares with a live story lives in their common base class, `AbstractGroupCall`; what only a video chat offers (title, scheduling, server-side recording, raising a hand, kicking) lives on `GroupCall` itself.

```php
use danog\MadelineProto\LocalFile;
use danog\MadelineProto\LocalDirectory;
use danog\MadelineProto\MediaDestination;
use danog\MadelineProto\ParseMode;
use danog\MadelineProto\RemoteUrl;

// Create a video chat in a group or channel we administer (or a scheduled one, or an RTMP livestream)...
$call = $this->createGroupCall('@mygroup', title: 'Weekly meeting');
// ...or join the one currently active there, optionally as one of our channels.
$call = $this->joinGroupCall('@mygroup', muted: false, joinAs: '@mychannel');

// Playback and recording work exactly like in one-to-one calls.
$call->play(new RemoteUrl('http://icestreaming.rai.it/1.mp3'));
$call->play(new LocalFile('slides.webm'), MediaDestination::Presentation); // screen-share
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

Scheduled calls can be started early with `startScheduled()`, and `setStartSubscription(true)` asks for a notification when they start. `getGroupCallJoinAs($peer)` lists the peers we may join a call as, and `saveDefaultGroupCallJoinAs($peer, $joinAs)` stores the default.

Your event handler receives a `GroupCall` update whenever a call starts, changes or ends, a `GroupCallParticipants` update when participants join, leave or change state, a `GroupCallMessage` update for every in-call message or reaction, and a `GroupCallMessagesDeleted` update when messages are deleted:

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

Large livestreams (and every RTMP livestream) are received in [stream mode](https://core.telegram.org/api/group-calls#stream-mode): the server serves the mixed media as downloadable chunks rather than over WebRTC. `isStreamMode()` tells whether a call is in stream mode; nothing can be transmitted in it, but it can be recorded with `setOutput()` without specifying a participant: an RTMP livestream's audio and video into a `.mkv`/`.webm` file (or its audio into a `.ogg`), and an automatically-scaled livestream's mixed audio into any format. Recording into a directory with `setOutputFolder()` writes the mixed stream to `stream.mkv` (or `.ogg`) and additionally each publisher's video of an automatically-scaled livestream to `video-<endpoint>.mkv`. The MP4 segments the server uses are demuxed in pure PHP by the `Mp4` class, which can also be used on its own.

To publish an RTMP livestream, get the RTMP URL and stream key with `getGroupCallStreamRtmpUrl($peer)`, then create the call with `createGroupCall($peer, rtmpStream: true)` and publish to it with any RTMP tool (OBS, ffmpeg...).

### Live stories

A [live story](https://core.telegram.org/api/group-calls#live-stories) is a livestream posted as a story, of which we are the only publisher: `startLive($peer, caption: 'Hi!')` starts one and returns a `LiveStory`, which is used like any other group call (`play()` to stream, `sendMessage()` and `sendReaction()` to comment) and arrives in event handlers as a `LiveStory` update. Viewers may donate Telegram Stars: `setPaidMessagesStars($stars)` sets the minimum donation required to comment, `donate($stars)` donates, and `getStars()` returns the donations received so far and the top donors.

## Conference calls

[Conference calls](https://core.telegram.org/api/group-calls#conference-calls) are end-to-end encrypted multi-party calls not associated with any group, handled through the `ConferenceCall` object, which implements the same `MultiCall` interface:

```php
// Create one (we are its only participant until someone joins)...
$call = $this->createConferenceCall();
$link = $call->exportInvite();          // https://t.me/call/... link anyone can join with
$call->invite('@alice');                 // or ring someone directly

// ...or join one from a link, or from an invitation service message.
$call = $this->joinConferenceCallBySlug('abcdef');
$call = $this->joinConferenceCallByInviteMessage($msgId);

$call->play(new LocalFile('song.ogg'));
$call->setOutputFolder(new LocalDirectory('recordings')); // decrypted, one numbered .mkv series per participant
$call->setOutput(new LocalFile('alice.mkv'), '@alice');    // decrypted, a single participant

// The key verification emojis, which every participant must compare.
$emojis = $call->getVisualization();

$call->sendMessage('Hi!');               // end-to-end encrypted in-call message
$call->removeParticipant('@intruder');   // rekeys, so they cannot decrypt anything any more
$call->leave();
```

Invitations arrive as `DialogConferenceCall` service messages, which can be accepted with `join()` or declined with `decline()`. A one-to-one call can be upgraded to a conference with `migrateCallToConference($callId)`.

<a href="https://docs.madelineproto.xyz/docs/FILES.html">Next section</a>