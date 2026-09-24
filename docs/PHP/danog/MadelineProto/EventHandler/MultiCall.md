---
title: "danog\\MadelineProto\\EventHandler\\MultiCall: Common interface for the multi-party call types — {@see Calls\\GroupCall} (video chats, livestreams),"
description: "{@see Calls\\LiveStory} (live stories) and {@see Calls\\ConferenceCall} (end-to-end encrypted conference\ncalls) — on top of the surface every call shares ({@see Call}).\n\nIt covers what a call with more than two participants adds over a one-to-one {@see Calls\\PrivateCall} call:\nleaving without ending it for everyone else, managing who is in it (inviting, invite links, removing\nparticipants), its title and settings, and messaging its participants. What only some call types\noffer (server-side recording, scheduling, raising a hand, moderating messages, donations) lives on the\nconcrete classes: {@see Calls\\AbstractGroupCall} for everything a video chat and a live story share,\n{@see Calls\\GroupCall} and {@see Calls\\LiveStory} for their own.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\MultiCall`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Common interface for the multi-party call types — {@see Calls\GroupCall} (video chats, livestreams),  

{@see Calls\LiveStory} (live stories) and {@see Calls\ConferenceCall} (end-to-end encrypted conference
calls) — on top of the surface every call shares ({@see Call}).

It covers what a call with more than two participants adds over a one-to-one {@see Calls\PrivateCall} call:
leaving without ending it for everyone else, managing who is in it (inviting, invite links, removing
participants), its title and settings, and messaging its participants. What only some call types
offer (server-side recording, scheduling, raising a hand, moderating messages, donations) lives on the
concrete classes: {@see Calls\AbstractGroupCall} for everything a video chat and a live story share,
{@see Calls\GroupCall} and {@see Calls\LiveStory} for their own.



## Method list:
* [`getParticipants(): array<int, TParticipant>`](#getParticipants)
* [`getParticipant(string|int $participant): (TParticipant|null)`](#getParticipant)
* [`leave(): static`](#leave)
* [`setTitle(string $title): static`](#setTitle)
* [`invite((string|int) ...$users): static`](#invite)
* [`exportInvite(bool $canSelfUnmute = false): string`](#exportInvite)
* [`removeParticipant((string|int) ...$participants): static`](#removeParticipant)
* [`sendMessage(string $message, (\danog\MadelineProto\ParseMode|null) $parseMode = NULL, (int|null) $paidStars = NULL, (string|int|null) $sendAs = NULL): static`](#sendMessage)
* [`sendReaction(string $emoji, (int|null) $customEmojiId = NULL): static`](#sendReaction)
* [`setMessagesEnabled(bool $enabled): static`](#setMessagesEnabled)
* [`muteParticipant(string|int $participant, bool $muted = true): static`](#muteParticipant)
* [`setParticipantVolume(string|int $participant, int<1, 20000> $volume): static`](#setParticipantVolume)
* [`setVideoPaused(bool $paused): static`](#setVideoPaused)
* [`setJoinMuted(bool $joinMuted): static`](#setJoinMuted)
* [`resetInviteHash(): static`](#resetInviteHash)
* [`isStreamMode(): bool`](#isStreamMode)
* [`isRtmpMode(): bool`](#isRtmpMode)
* [`join(bool $muted = false): static`](#join)
* [`discard(): static`](#discard)
* [`isJoined(): bool`](#isJoined)
* [`getCallState(): \danog\MadelineProto\VoIP\CallState|\danog\MadelineProto\EventHandler\Calls\GroupCallState`](#getCallState)
* [`getVisualization(): (list<string>|null)`](#getVisualization)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#play)
* [`playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#playBlocking)
* [`then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#then)
* [`playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`](#playOnHold)
* [`skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#skip)
* [`stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#stop)
* [`pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#pause)
* [`isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`](#isPaused)
* [`resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#resume)
* [`getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#getCurrent)
* [`setMuted(bool $muted = true): static`](#setMuted)
* [`isMuted(): bool`](#isMuted)
* [`enablePresentation(): static`](#enablePresentation)
* [`disablePresentation(): static`](#disablePresentation)
* [`isSharingScreen(): bool`](#isSharingScreen)
* [`setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, (StreamMask|null) $streams = NULL): StreamMask`](#setOutput)
* [`setOutputFolder(\danog\MadelineProto\LocalDirectory $dir, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): static`](#setOutputFolder)

## Methods:
### <a name="getParticipants"></a> `getParticipants(): array<int, TParticipant>`

The participants currently known to be in the call, keyed by their bot API id.
  
The element type is call-type specific: a {@see Calls\GroupCallParticipant} (or, for a live  
story, a {@see Calls\LiveStoryParticipant}) for a group call, a {@see Calls\ConferenceCallParticipant}  
for a conference.  


#### See also: 
* `TParticipant`




### <a name="getParticipant"></a> `getParticipant(string|int $participant): (TParticipant|null)`

A participant of the call by their id, username or peer, or null if they are not in it.


Parameters:

* `$participant`: `string|int`   


#### See also: 
* `TParticipant`




### <a name="leave"></a> `leave(): static`

Leave the call, keeping it running for the other participants (unlike {@see Call::discard()},
which ends it).  



### <a name="setTitle"></a> `setTitle(string $title): static`

Change the title of the call.


Parameters:

* `$title`: `string`   



### <a name="invite"></a> `invite((string|int) ...$users): static`

Invite users to the call.


Parameters:

* `...$users`: `(string|int)` The users to invite (user ids, usernames or peers).  



### <a name="exportInvite"></a> `exportInvite(bool $canSelfUnmute = false): string`

Export an invite link to the call.


Parameters:

* `$canSelfUnmute`: `bool` Whether users joining with this link may speak without asking; ignored where the call has no such distinction.  



### <a name="removeParticipant"></a> `removeParticipant((string|int) ...$participants): static`

Remove participants from the call.


Parameters:

* `...$participants`: `(string|int)` The participants to remove (user ids, usernames or peers).  



### <a name="sendMessage"></a> `sendMessage(string $message, (\danog\MadelineProto\ParseMode|null) $parseMode = NULL, (int|null) $paidStars = NULL, (string|int|null) $sendAs = NULL): static`

Send an [in-call message »](https://core.telegram.org/api/group-calls#in-call-messages) to the
participants of the call, shown as an overlay by their clients (there is no chat history).  


Parameters:

* `$message`: `string` The text; markup in `$parseMode` is converted to entities.  
* `$parseMode`: `(\danog\MadelineProto\ParseMode|null)` Whether to parse HTML or Markdown markup in the text.  
* `$paidStars`: `(int|null)` Live stories only: Telegram Stars to donate with the message (at least the story's minimum, see {@see Calls\LiveStory::setPaidMessagesStars()}).  
* `$sendAs`: `(string|int|null)` Live stories only: the peer to send the message as.  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../../danog/MadelineProto/ParseMode.html)




### <a name="sendReaction"></a> `sendReaction(string $emoji, (int|null) $customEmojiId = NULL): static`

Send an [in-call reaction »](https://core.telegram.org/api/group-calls#in-call-reactions): a
single emoji, or a custom emoji (with the fallback emoji as `$emoji`).  


Parameters:

* `$emoji`: `string` The emoji.  
* `$customEmojiId`: `(int|null)` The document id of a custom emoji to send instead, `$emoji` being its fallback.  



### <a name="setMessagesEnabled"></a> `setMessagesEnabled(bool $enabled): static`

Enable or disable in-call messages (admins only).


Parameters:

* `$enabled`: `bool`   



### <a name="muteParticipant"></a> `muteParticipant(string|int $participant, bool $muted = true): static`

Mute or unmute a participant (admins only), or, for a non-admin, mute a participant only for
ourselves. A participant muted by an admin may not unmute themselves.  


Parameters:

* `$participant`: `string|int`   
* `$muted`: `bool`   



### <a name="setParticipantVolume"></a> `setParticipantVolume(string|int $participant, int<1, 20000> $volume): static`

Set our local playback volume of a participant.


Parameters:

* `$participant`: `string|int`   
* `$volume`: `int<1, 20000>` From 1 to 20000, where 10000 is 100%.  



### <a name="setVideoPaused"></a> `setVideoPaused(bool $paused): static`

Pause or resume our own video stream, telling the other participants to keep showing the last
frame rather than hiding it.  


Parameters:

* `$paused`: `bool`   



### <a name="setJoinMuted"></a> `setJoinMuted(bool $joinMuted): static`

Whether new participants join muted (admins only).


Parameters:

* `$joinMuted`: `bool`   



### <a name="resetInviteHash"></a> `resetInviteHash(): static`

Invalidate every invite link exported so far (admins only).



### <a name="isStreamMode"></a> `isStreamMode(): bool`

Whether the server switched us to [stream mode »](https://core.telegram.org/api/group-calls#stream-mode):
the call's media is received by downloading chunks rather than over WebRTC, and there is a single  
mixed stream to record (see {@see Call::setOutput()} and {@see Call::setOutputFolder()}) rather than one per participant.  



### <a name="isRtmpMode"></a> `isRtmpMode(): bool`

Whether the call's media is published by a single external RTMP publisher (an RTMP livestream).



### <a name="join"></a> `join(bool $muted = false): static`

Join the call: accept an incoming one-to-one call, or join a multi-party call.


Parameters:

* `$muted`: `bool` Whether to join with our own audio muted.  



### <a name="discard"></a> `discard(): static`

Discard the call: hang up a one-to-one call, or end a multi-party call for every participant
(see {@see MultiCall::leave()} to leave one without ending it).  



### <a name="isJoined"></a> `isJoined(): bool`

Whether we are currently in the call: a one-to-one call that is running, or a multi-party
call we joined and did not leave.  



### <a name="getCallState"></a> `getCallState(): \danog\MadelineProto\VoIP\CallState|\danog\MadelineProto\EventHandler\Calls\GroupCallState`

The state of the call: a {@see CallState} for a one-to-one call, a {@see GroupCallState} for a
multi-party call.  


#### See also: 
* [\danog\MadelineProto\VoIP\CallState](../../../danog/MadelineProto/VoIP/CallState.html)
* [`\danog\MadelineProto\EventHandler\Calls\GroupCallState`: State of a group call we are interacting with.](../../../danog/MadelineProto/EventHandler/Calls/GroupCallState.html)




### <a name="getVisualization"></a> `getVisualization(): (list<string>|null)`

The key verification emojis of an end-to-end encrypted call (a one-to-one call or a conference),
which every participant can compare to make sure nobody is in the middle.  
  
Returns null until the key is established (and, for a conference, every participant has taken  
part in the verification), and always for a call that is not end-to-end encrypted (a video chat  
or livestream).  



### <a name="play"></a> `play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play a file, transmitting its audio and, if it carries a transmittable one, its video.
  
A WebM/Matroska file with VP8, VP9, H.264 or AV1 video has its video transmitted too; any other  
file (or a raw audio stream) is played as audio only. Frames are demuxed in pure PHP and sent  
as-is where possible, so no transcoding (and thus no FFI extension) is required for pre-encoded  
WebM/OGG-OPUS input. `$dest` selects the camera or the presentation (screencast) stream.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)




### <a name="playBlocking"></a> `playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play a file like {@see self::play()}, but block until it has finished playing if a stream was passed.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)




### <a name="then"></a> `then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Add a file to the playlist, to be played once the current one finishes.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)




### <a name="playOnHold"></a> `playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`

Set the files to play, on loop, while the given stream's main playlist is empty.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="skip"></a> `skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Skip to the next file in the playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)




### <a name="stop"></a> `stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Stop playing all files, clearing the main and the hold playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)




### <a name="pause"></a> `pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Pause playback of the current file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)




### <a name="isPaused"></a> `isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`

Whether playback of the current file is paused.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)




### <a name="resume"></a> `resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Resume playback of the current file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)




### <a name="getCurrent"></a> `getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

The file or stream currently being played, if any.
  
Returns a string with the object ID of the stream if a stream is playing, otherwise the related  
{@see LocalFile} or {@see RemoteUrl}.  


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../danog/MadelineProto/LocalFile.html)




### <a name="setMuted"></a> `setMuted(bool $muted = true): static`

Mute or unmute our own outgoing audio.


Parameters:

* `$muted`: `bool`   



### <a name="isMuted"></a> `isMuted(): bool`

Whether our own outgoing audio is muted.



### <a name="enablePresentation"></a> `enablePresentation(): static`

Start sharing a screen: bring up the presentation (screencast) stream, so that files played on
{@see MediaDestination::Presentation} are transmitted as a screen-share. Idempotent, and done  
automatically by the first playback on the presentation stream.  



### <a name="disablePresentation"></a> `disablePresentation(): static`

Stop sharing the screen, dropping the presentation playlist.



### <a name="isSharingScreen"></a> `isSharingScreen(): bool`

Whether a screen-share is currently being transmitted.



### <a name="setOutput"></a> `setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, (StreamMask|null) $streams = NULL): StreamMask`

Record the incoming media of a participant into one file (or stream) with a fixed set of tracks.
  
A participant sends up to three streams — their microphone audio, their camera video and their  
screen share (a second video track), see {@see CallStream} — and may turn any of them on or off  
at any time. `$streams` picks which of them the recording holds, as a bitmask of  
{@see CallStream::AUDIO}, {@see CallStream::VIDEO} and {@see CallStream::SCREEN}; every chosen  
stream must be available (sent by the participant right now, see {@see Calls\CallStreams}) or an  
exception is thrown. When `$streams` is null, every available stream is recorded (and if none is,  
an exception is thrown). Either way the streams currently available are returned.  
  
A Matroska file's track list is fixed in its header, so the file keeps its tracks for its whole  
duration: a stream the participant turns off simply stops being written, and is written again when  
it comes back; a stream that becomes available later is not added (call this method again to start  
a new file with it). Only two things finish the file early: a change of codec of one of its video  
streams, or the end of the call (or our leaving it). Every start and end of a recording, and every  
change of the available streams or their codecs, is reported by a {@see Calls\CallStreams} update.  
  
`$file` is where to record to: a {@see LocalFile}, or a {@see WritableStream}. `$participant` is  
who to record: in a one-to-one call it may only be the other party, and is therefore optional;  
in a multi-party call it is required, every participant being recorded to its own file (see  
{@see self::setOutputFolder()} to record everyone at once) — except in  
[stream mode »](https://core.telegram.org/api/group-calls#stream-mode), where the call is a  
single mixed stream, recorded without specifying a participant. Our own media is never recorded.  
  
A {@see RecordingFormat::Webm} or {@see RecordingFormat::Mkv} target muxes the media into a  
Matroska file in pure PHP: the frames are stored as-is, so the video tracks are whatever codec the  
participant sends (VP8/VP9/H.264/H.265/AV1) and the audio is OPUS. {@see RecordingFormat::Opus} writes  
an audio-only OGG OPUS stream, and is supported by one-to-one calls (and stream mode) only. When  
`$format` is null it is autodetected from the extension of `$file` if a {@see LocalFile} was passed;  
a raw stream, whose extension is unknown, defaults to WebM.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream`   
* `$participant`: `string|int|null`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   
* `$streams`: `(StreamMask|null)` The streams to record, as a bitmask of {@see CallStream} flags, or null for every available one.  


Return value: The streams the participant currently sends, as a bitmask of {@see CallStream} flags.

#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../danog/MadelineProto/LocalFile.html)
* `\Amp\ByteStream\WritableStream`
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../../danog/MadelineProto/RecordingFormat.html)
* `StreamMask`




### <a name="setOutputFolder"></a> `setOutputFolder(\danog\MadelineProto\LocalDirectory $dir, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): static`

Record the incoming media of the call into a directory, following every change of the streams.
  
Unlike {@see self::setOutput()}, whose file keeps a fixed set of tracks, a directory recording  
follows the participants turning their microphone, camera and screen share on and off: since a  
Matroska file's track list is fixed in its header, every such change closes the current file and  
continues in a new one, so each participant's recording is a numbered series of files, each named  
after the streams it holds: `<n>_<streams>.mkv`, with `n` counting from 0 and `streams` listing  
`audio`, `video` and `screen` (joined by commas, in that order): `0_audio.mkv`, `1_audio,video.mkv`,  
`2_audio,video,screen.mkv`, …. Every file opened and finished is reported by a {@see Calls\CallStreams} update.  
  
In a one-to-one call the other party is recorded as `<dir>/<n>_<streams>.mkv`. In a multi-party  
call every participant that transmits something (including ones that start later) is recorded as  
`<dir>/<peerId>.<n>_<streams>.mkv`, or only the one given as `$participant` (a user id, username  
or peer) if any; our own media is never recorded. In  
[stream mode »](https://core.telegram.org/api/group-calls#stream-mode) the mixed stream is recorded  
as `<dir>/stream.mkv` (`.webm`, or `.ogg` for {@see RecordingFormat::Opus}) and, in an  
automatically-scaled livestream, each publisher's video as `<dir>/video-<endpoint>.mkv`.  
  
The files are Matroska ({@see RecordingFormat::Mkv} by default, or {@see RecordingFormat::Webm}).  


Parameters:

* `$dir`: `\danog\MadelineProto\LocalDirectory`   
* `$participant`: `string|int|null`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   


#### See also: 
* [`\danog\MadelineProto\LocalDirectory`: Indicates a local directory to write output into.](../../../danog/MadelineProto/LocalDirectory.html)
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../../danog/MadelineProto/RecordingFormat.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
