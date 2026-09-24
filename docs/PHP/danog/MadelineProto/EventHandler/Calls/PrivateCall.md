---
title: "danog\\MadelineProto\\EventHandler\\Calls\\PrivateCall: This update represents a private (one-to-one) VoIP Telegram call."
description: "\nThe old name {@see \\danog\\MadelineProto\\VoIP} is kept as an alias for backwards compatibility.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Calls\PrivateCall`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

This update represents a private (one-to-one) VoIP Telegram call.  


The old name {@see \danog\MadelineProto\VoIP} is kept as an alias for backwards compatibility.


## Properties
* `$callID`: `int` Phone call ID
* `$outgoing`: `bool` Whether the call is an outgoing call
* `$video`: `bool` Whether this is a video call.
* `$otherID`: `int` ID of the other user in the call
* `$date`: `int` When was the call created
* `$discardReason`: `?danog\MadelineProto\VoIP\DiscardReason` Why the call was discarded, if it was.
* `$conferenceSlug`: `?string` If the call was upgraded to a [conference call »](https://core.telegram.org/api/group-calls#conference-calls),
the [conference deep link »](https://core.telegram.org/api/links#conference-links) slug of the new conference.

Conference calls are end-to-end encrypted and cannot be joined by MadelineProto yet.

## Method list:
* [`join(bool $muted = false): static`](#join)
* [`discard(\danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<1, 5> $rating = NULL, string $comment = NULL): static`](#discard)
* [`isJoined(): bool`](#isJoined)
* [`getCallState(): \danog\MadelineProto\VoIP\CallState`](#getCallState)
* [`getRemoteMediaState(): ?\danog\MadelineProto\VoIP\MediaState`](#getRemoteMediaState)
* [`getVisualization(): ?list{string, string, string, string}`](#getVisualization)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#play)
* [`playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#playBlocking)
* [`setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, (StreamMask|null) $streams = NULL): StreamMask`](#setOutput)
* [`setOutputFolder(\danog\MadelineProto\LocalDirectory $dir, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): static`](#setOutputFolder)
* [`then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#then)
* [`skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#skip)
* [`stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#stop)
* [`pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#pause)
* [`isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`](#isPaused)
* [`resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#resume)
* [`playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`](#playOnHold)
* [`getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#getCurrent)
* [`setMuted(bool $muted = true): static`](#setMuted)
* [`isMuted(): bool`](#isMuted)
* [`enablePresentation(): static`](#enablePresentation)
* [`disablePresentation(): static`](#disablePresentation)
* [`isSharingScreen(): bool`](#isSharingScreen)

## Methods:
### <a name="join"></a> `join(bool $muted = false): static`

Accept the incoming call.


Parameters:

* `$muted`: `bool` Whether to accept with our own audio muted.  



### <a name="discard"></a> `discard(\danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<1, 5> $rating = NULL, string $comment = NULL): static`

Discard call.


Parameters:

* `$reason`: `\danog\MadelineProto\VoIP\DiscardReason`   
* `$rating`: `int<1, 5>` Call rating in stars  
* `$comment`: `string` Additional comment on call quality.  


#### See also: 
* [`\danog\MadelineProto\VoIP\DiscardReason`: Why was the call discarded?](../../../../danog/MadelineProto/VoIP/DiscardReason.html)




### <a name="isJoined"></a> `isJoined(): bool`

Whether the call is running (accepted by both parties and connected).



### <a name="getCallState"></a> `getCallState(): \danog\MadelineProto\VoIP\CallState`

Get call state.


#### See also: 
* [\danog\MadelineProto\VoIP\CallState](../../../../danog/MadelineProto/VoIP/CallState.html)




### <a name="getRemoteMediaState"></a> `getRemoteMediaState(): ?\danog\MadelineProto\VoIP\MediaState`

The other party of the call, keyed by their user ID, with their media state (mute, camera and
screencast status) as reported by their client.  
  
Empty until the call is connected and the other party has reported their media state.  


#### See also: 
* [`\danog\MadelineProto\VoIP\MediaState`: The media state of the other party of a one-to-one call, as reported by its `MediaState`](../../../../danog/MadelineProto/VoIP/MediaState.html)




### <a name="getVisualization"></a> `getVisualization(): ?list{string, string, string, string}`

Get the key verification emojis (will return null if the call is not inited yet).



### <a name="play"></a> `play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play a file, transmitting its audio and, if it carries a transmittable one, its video.
  
A WebM/Matroska file with VP8, VP9 or H.264 video has its video transmitted too; any other  
file (or a raw audio stream) is played as audio only. The file is demuxed in pure PHP and its  
frames are sent as-is where possible, so no transcoding (and thus no FFI extension) is  
required for pre-encoded WebM/OGG-OPUS input.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="playBlocking"></a> `playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play a file, blocking until it has finished playing if a stream is provided.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="setOutput"></a> `setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, (StreamMask|null) $streams = NULL): StreamMask`

Record the other party into one file (or stream) with a fixed set of tracks.
  
The file holds the streams chosen with `$streams` — a bitmask of {@see CallStream::AUDIO},  
{@see CallStream::VIDEO} and {@see CallStream::SCREEN}, every one of which must be available — or,  
when null, every stream the other party currently sends; the available streams are returned. The  
tracks are fixed for the whole file: a stream turned off stops being written and resumes when it  
comes back, and only a change of codec or the end of the call finishes the file (see  
{@see Call::setOutput()}); every such event is reported by a {@see CallStreams} update.  
`$participant` may only be the other party, and is therefore optional.  
  
A {@see RecordingFormat::Webm} or {@see RecordingFormat::Mkv} target records the chosen streams,  
muxed into a Matroska file in pure PHP (the peer's frames are stored as-is, so the video tracks are  
whatever codec the peer sends — VP8/VP9/H.264/H.265/AV1 — and the audio is OPUS).  
{@see RecordingFormat::Opus} writes an audio-only OGG OPUS stream (so only {@see CallStream::AUDIO}  
may be chosen); it is the only format the legacy libtgvoip engine, negotiated by very old clients,  
supports. When `$format` is null it is autodetected from the extension of `$file`, but only if a  
{@see LocalFile} was passed; a raw stream, whose extension is unknown, defaults to WebM.  
  
Before the call is connected (the other party has not reported what it sends yet) any set of  
streams is accepted, the recording starts with the chosen ones once media flows, and 0 is returned.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream`   
* `$participant`: `string|int|null`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   
* `$streams`: `(StreamMask|null)` The streams to record, as a bitmask of {@see CallStream} flags, or null for every available one.  


Return value: The streams the other party currently sends, as a bitmask of {@see CallStream} flags.

#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* `\Amp\ByteStream\WritableStream`
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../../../danog/MadelineProto/RecordingFormat.html)
* `StreamMask`




### <a name="setOutputFolder"></a> `setOutputFolder(\danog\MadelineProto\LocalDirectory $dir, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): static`

Record the other party into a directory, as `<dir>/0_<streams>.mkv`, `<dir>/1_<streams>.mkv`, …:
one file per combination of streams (audio, camera, screencast) they send, a new one each time  
they turn one on or off (see {@see Call::setOutputFolder()}). `$participant` may only be the  
other party, and is therefore optional.  


Parameters:

* `$dir`: `\danog\MadelineProto\LocalDirectory`   
* `$participant`: `string|int|null`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   


#### See also: 
* [`\danog\MadelineProto\LocalDirectory`: Indicates a local directory to write output into.](../../../../danog/MadelineProto/LocalDirectory.html)
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../../../danog/MadelineProto/RecordingFormat.html)




### <a name="then"></a> `then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play file.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="skip"></a> `skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

When called, skips to the next file in the playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="stop"></a> `stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Stops playing all files, clears the main and the hold playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="pause"></a> `pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Pauses the currently playing file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="isPaused"></a> `isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`

Whether the currently playing file is paused.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="resume"></a> `resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Resumes the currently playing file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="playOnHold"></a> `playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`

Files to play on hold.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="getCurrent"></a> `getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

Get the file that is currently being played.
  
Will return a string with the object ID of the stream if we're currently playing a stream, otherwise returns the related LocalFile or RemoteUrl.  


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)




### <a name="setMuted"></a> `setMuted(bool $muted = true): static`

Mute or unmute our own audio stream.


Parameters:

* `$muted`: `bool`   



### <a name="isMuted"></a> `isMuted(): bool`

Whether our own audio stream is muted.



### <a name="enablePresentation"></a> `enablePresentation(): static`

Start sharing a screen: bring up the presentation (screencast) video stream, so that files played
on {@see MediaDestination::Presentation} are transmitted as a screencast. The other party is told  
the screencast is active as soon as a file with video plays on it.  



### <a name="disablePresentation"></a> `disablePresentation(): static`

Stop sharing the screen: stop the presentation playlist and tell the other party the screencast
is inactive.  



### <a name="isSharingScreen"></a> `isSharingScreen(): bool`

Whether a screencast is currently being transmitted.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
