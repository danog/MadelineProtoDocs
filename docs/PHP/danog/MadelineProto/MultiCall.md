---
title: "danog\\MadelineProto\\MultiCall: Common interface for the multi-party call types — {@see GroupCall} (video chats, livestreams) and"
description: "{@see \\danog\\MadelineProto\\Tgcalls\\E2E\\ConferenceCall} (end-to-end encrypted conference calls) — on\ntop of the media surface every call shares ({@see Call}).\n\nIt covers what a call with more than two participants adds over a one-to-one {@see VoIP} call:\nleaving without ending it for everyone else, and enumerating who is in it. Type-specific operations\n(a group call's {@see GroupCall::invite()} / per-participant recording, a conference's\nverification emojis / encrypted messages / participant removal) live on the concrete classes.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\MultiCall`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Common interface for the multi-party call types — {@see GroupCall} (video chats, livestreams) and  

{@see \danog\MadelineProto\Tgcalls\E2E\ConferenceCall} (end-to-end encrypted conference calls) — on
top of the media surface every call shares ({@see Call}).

It covers what a call with more than two participants adds over a one-to-one {@see VoIP} call:
leaving without ending it for everyone else, and enumerating who is in it. Type-specific operations
(a group call's {@see GroupCall::invite()} / per-participant recording, a conference's
verification emojis / encrypted messages / participant removal) live on the concrete classes.



## Method list:
* [`leave(): static`](#leave)
* [`getParticipants(): array<int, mixed>`](#getParticipants)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#play)
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
* [`discard(): static`](#discard)

## Methods:
### <a name="leave"></a> `leave(): static`

Leave the call, keeping it running for the other participants (unlike {@see Call::discard()},
which ends it).  



### <a name="getParticipants"></a> `getParticipants(): array<int, mixed>`

The participants currently known to be in the call, keyed by their id. The element type is
call-type specific (a {@see GroupCall\Participant} for a group call, chain state for a  
conference), so the concrete class documents it.  



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
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="then"></a> `then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Add a file to the playlist, to be played once the current one finishes.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="playOnHold"></a> `playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`

Set the files to play, on loop, while the given stream's main playlist is empty.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="skip"></a> `skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Skip to the next file in the playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="stop"></a> `stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Stop playing all files, clearing the main and the hold playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="pause"></a> `pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Pause playback of the current file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="isPaused"></a> `isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`

Whether playback of the current file is paused.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="resume"></a> `resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Resume playback of the current file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="getCurrent"></a> `getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

The file or stream currently being played, if any.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)




### <a name="setMuted"></a> `setMuted(bool $muted = true): static`

Mute or unmute our own outgoing audio.


Parameters:

* `$muted`: `bool`   



### <a name="isMuted"></a> `isMuted(): bool`

Whether our own outgoing audio is muted.



### <a name="discard"></a> `discard(): static`

Discard (hang up / leave) the call.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
