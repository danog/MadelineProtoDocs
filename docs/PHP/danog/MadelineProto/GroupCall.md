---
title: "danog\\MadelineProto\\GroupCall: This update represents a Telegram group call (a video chat, a livestream or a live story)."
description: "\nSee https://core.telegram.org/api/group-calls for more info.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\GroupCall`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

This update represents a Telegram group call (a video chat, a livestream or a live story).  


See https://core.telegram.org/api/group-calls for more info.


## Properties
* `$id`: `int` Group call ID.
* `$accessHash`: `int` Access hash of the group call.
* `$peerId`: `?int` Bot API ID of the group/channel the call is associated with, if any.
* `$title`: `?string` Title of the call, if it has one.
* `$participantsCount`: `int` Number of participants.
* `$joinMuted`: `bool` Whether new participants join muted.
* `$rtmpStream`: `bool` Whether this is an RTMP livestream.
* `$conference`: `bool` Whether this is an E2E-encrypted conference call, not associated with any group.
* `$creator`: `bool` Whether we created this call.
* `$inviteLink`: `?string` The invite link of a conference call, if any.
* `$scheduleDate`: `?int` When the call is scheduled to start, if it is a scheduled call.
* `$streamDcId`: `?int` The DC to use when downloading media chunks in stream mode.
* `$discarded`: `bool` Whether the call has ended.

## Method list:
* [`join(bool $muted = false, mixed $joinAs = NULL, (string|null) $inviteHash = NULL): \danog\MadelineProto\GroupCall`](#join)
* [`leave(): \danog\MadelineProto\GroupCall`](#leave)
* [`discard(): \danog\MadelineProto\GroupCall`](#discard)
* [`getCallState(): \danog\MadelineProto\GroupCall\GroupCallState`](#getCallState)
* [`getParticipants(): array<int, \danog\MadelineProto\GroupCall\Participant>`](#getParticipants)
* [`setMuted(bool $muted = true): \danog\MadelineProto\GroupCall`](#setMuted)
* [`isMuted(): bool`](#isMuted)
* [`setTitle(string $title): \danog\MadelineProto\GroupCall`](#setTitle)
* [`invite(mixed ...$users): \danog\MadelineProto\GroupCall`](#invite)
* [`exportInvite(bool $canSelfUnmute = false): string`](#exportInvite)
* [`setOutput(mixed $participant, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream|null $file = NULL): \danog\MadelineProto\GroupCall`](#setOutput)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`](#play)
* [`playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`](#playBlocking)
* [`then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`](#then)
* [`skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`](#skip)
* [`stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`](#stop)
* [`pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`](#pause)
* [`isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`](#isPaused)
* [`resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`](#resume)
* [`playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): \danog\MadelineProto\GroupCall`](#playOnHold)
* [`getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#getCurrent)

## Methods:
### <a name="join"></a> `join(bool $muted = false, mixed $joinAs = NULL, (string|null) $inviteHash = NULL): \danog\MadelineProto\GroupCall`

Join the group call.
  
Note that [conference calls »](https://core.telegram.org/api/group-calls#conference-calls) are  
end-to-end encrypted and are not supported yet.  


Parameters:

* `$muted`: `bool` Whether to join muted.  
* `$joinAs`: `mixed` Peer to join as; only [video chats/livestreams »](https://core.telegram.org/api/group-calls#video-chats-livestreams) may use a peer other than ourselves.  
* `$inviteHash`: `(string|null)` Invite hash from a [video chat invite link »](https://core.telegram.org/api/links#video-chat-livestream-links), if any.  



### <a name="leave"></a> `leave(): \danog\MadelineProto\GroupCall`

Leave the group call, without ending it for the other participants.



### <a name="discard"></a> `discard(): \danog\MadelineProto\GroupCall`

End the group call for all participants.



### <a name="getCallState"></a> `getCallState(): \danog\MadelineProto\GroupCall\GroupCallState`

Get the state of the group call.


#### See also: 
* [`\danog\MadelineProto\GroupCall\GroupCallState`: State of a group call we are interacting with.](../../danog/MadelineProto/GroupCall/GroupCallState.html)




### <a name="getParticipants"></a> `getParticipants(): array<int, \danog\MadelineProto\GroupCall\Participant>`

Get all known participants, indexed by their bot API peer ID.


#### See also: 
* [`\danog\MadelineProto\GroupCall\Participant`: A participant of a group call, mirroring](../../danog/MadelineProto/GroupCall/Participant.html)




### <a name="setMuted"></a> `setMuted(bool $muted = true): \danog\MadelineProto\GroupCall`

Mute or unmute our own audio stream.


Parameters:

* `$muted`: `bool`   



### <a name="isMuted"></a> `isMuted(): bool`

Whether our own audio stream is muted.



### <a name="setTitle"></a> `setTitle(string $title): \danog\MadelineProto\GroupCall`

Change the title of the group call.


Parameters:

* `$title`: `string`   



### <a name="invite"></a> `invite(mixed ...$users): \danog\MadelineProto\GroupCall`

Invite users to the group call.


Parameters:

* `...$users`: `mixed`   



### <a name="exportInvite"></a> `exportInvite(bool $canSelfUnmute = false): string`

Export an invite link for this group call.


Parameters:

* `$canSelfUnmute`: `bool` Whether users joining with this link may speak without asking; admins only.  



### <a name="setOutput"></a> `setOutput(mixed $participant, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream|null $file = NULL): \danog\MadelineProto\GroupCall`

Record group call audio, writing an OGG OPUS stream.
  
Call it either way:  
 - `setOutput($participant, $file)` records that one participant's incoming audio to the file  
   or stream.  
 - `setOutput(new LocalDirectory($dir))` records *every* transmitting participant, each into its  
   own `<dir>/<peerId>.ogg` file (participants that start transmitting later are picked up too);  
   our own audio is never recorded.  


Parameters:

* `$participant`: `mixed`   
* `$file`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream|null`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* `\Amp\ByteStream\WritableStream`




### <a name="play"></a> `play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`

Play a file, transmitting its audio and, if it carries a transmittable one, its video.
  
A WebM/Matroska file with VP8, VP9 or H.264 video has its video transmitted too; any other  
file (or a raw audio stream) is played as audio only. Frames are demuxed in pure PHP and sent  
as-is where possible, so no transcoding (and thus no FFI extension) is required for  
pre-encoded WebM/OGG-OPUS input.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="playBlocking"></a> `playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`

Play a file, blocking until it has finished playing if a stream is provided.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="then"></a> `then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`

Play file.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="skip"></a> `skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`

When called, skips to the next file in the playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="stop"></a> `stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`

Stops playing all files, clears the main and the hold playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="pause"></a> `pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`

Pauses the currently playing file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="isPaused"></a> `isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`

Whether the currently playing file is paused.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="resume"></a> `resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\GroupCall`

Resumes the currently playing file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)




### <a name="playOnHold"></a> `playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): \danog\MadelineProto\GroupCall`

Files to play on hold.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="getCurrent"></a> `getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

Get the file that is currently being played.
  
Will return a string with the object ID of the stream if we're currently playing a stream,  
otherwise returns the related LocalFile or RemoteUrl.  


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
