---
title: "danog\\MadelineProto\\EventHandler\\Calls\\ConferenceCall: This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls)."
description: "\nUnlike a plain {@see GroupCall} (a video chat or livestream), a conference call is not associated\nwith any group or channel: it is a standalone, end-to-end encrypted multi-party call, whose media\nthe SFU only ever forwards as ciphertext. On top of the shared {@see MultiCall} surface it exposes\nthe conference-specific behaviour: the [emoji verification »](https://core.telegram.org/api/end-to-end/group-calls#verifying-the-key)\nof the key, end-to-end encrypted in-call messages, and removing participants by rekeying.\n\nThis is a thin, serializable handle: every operation is delegated to the live conference controller\n({@see \\danog\\MadelineProto\\Tgcalls\\E2E\\ConferenceCall}) by call ID, so it keeps working across a\nprocess restart and over IPC.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\EventHandler\Calls\ConferenceCall`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls).  


Unlike a plain {@see GroupCall} (a video chat or livestream), a conference call is not associated
with any group or channel: it is a standalone, end-to-end encrypted multi-party call, whose media
the SFU only ever forwards as ciphertext. On top of the shared {@see MultiCall} surface it exposes
the conference-specific behaviour: the [emoji verification »](https://core.telegram.org/api/end-to-end/group-calls#verifying-the-key)
of the key, end-to-end encrypted in-call messages, and removing participants by rekeying.

This is a thin, serializable handle: every operation is delegated to the live conference controller
({@see \danog\MadelineProto\Tgcalls\E2E\ConferenceCall}) by call ID, so it keeps working across a
process restart and over IPC.


## Properties
* `$id`: `int` Conference call ID.
* `$accessHash`: `int` Access hash of the conference call.
* `$participantsCount`: `int` Number of participants.
* `$creator`: `bool` Whether we created this call.
* `$inviteLink`: `?string` The invite link of the conference call, if any.
* `$messagesEnabled`: `bool` Whether in-call messages are enabled.
* `$unmutedVideoCount`: `?int` How many participants are transmitting video.
* `$unmutedVideoLimit`: `int` How many participants may transmit video at once.
* `$discarded`: `bool` Whether the call has ended.
* `$duration`: `?int` Duration of the call in seconds, once it has ended.

## Method list:
* [`join(bool $muted = false): static`](#join)
* [`isJoined(): bool`](#isJoined)
* [`getCallState(): \danog\MadelineProto\GroupCall\GroupCallState`](#getCallState)
* [`leave(): static`](#leave)
* [`discard(): static`](#discard)
* [`getParticipants(): array<int, array{public_key: string, permissions: int, version: int}>`](#getParticipants)
* [`getParticipant(mixed $participant): (array{public_key: string, permissions: int, version: int}|null)`](#getParticipant)
* [`removeParticipant(mixed ...$participants): static`](#removeParticipant)
* [`invite(mixed ...$users): static`](#invite)
* [`exportInvite(bool $canSelfUnmute = false): string`](#exportInvite)
* [`setTitle(string $title): static`](#setTitle)
* [`getVisualization(): (list<string>|null)`](#getVisualization)
* [`sendMessage(string $message, (\danog\MadelineProto\ParseMode|null) $parseMode = NULL, (int|null) $paidStars = NULL, mixed $sendAs = NULL): static`](#sendMessage)
* [`sendReaction(string $emoji, (int|null) $customEmojiId = NULL): static`](#sendReaction)
* [`setMessagesEnabled(bool $enabled): static`](#setMessagesEnabled)
* [`muteParticipant(mixed $participant, bool $muted = true): static`](#muteParticipant)
* [`setParticipantVolume(mixed $participant, int $volume): static`](#setParticipantVolume)
* [`setVideoPaused(bool $paused): static`](#setVideoPaused)
* [`setJoinMuted(bool $joinMuted): static`](#setJoinMuted)
* [`resetInviteHash(): static`](#resetInviteHash)
* [`isStreamMode(): bool`](#isStreamMode)
* [`isRtmpMode(): bool`](#isRtmpMode)
* [`isSharingScreen(): bool`](#isSharingScreen)
* [`enablePresentation(): static`](#enablePresentation)
* [`disablePresentation(): static`](#disablePresentation)
* [`setOutput(\danog\MadelineProto\LocalFile|\danog\MadelineProto\LocalDirectory|\Amp\ByteStream\WritableStream $file, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): static`](#setOutput)
* [`setMuted(bool $muted = true): static`](#setMuted)
* [`isMuted(): bool`](#isMuted)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#play)
* [`playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#playBlocking)
* [`then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#then)
* [`skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#skip)
* [`stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#stop)
* [`pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#pause)
* [`isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`](#isPaused)
* [`resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#resume)
* [`playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`](#playOnHold)
* [`getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#getCurrent)

## Methods:
### <a name="join"></a> `join(bool $muted = false): static`

Join the conference call.


Parameters:

* `$muted`: `bool` Whether to join muted.  



### <a name="isJoined"></a> `isJoined(): bool`

Whether we are currently in the conference (joined and not left/removed).



### <a name="getCallState"></a> `getCallState(): \danog\MadelineProto\GroupCall\GroupCallState`

Get the state of the conference call.


#### See also: 
* [`\danog\MadelineProto\GroupCall\GroupCallState`: State of a group call we are interacting with.](../../../../danog/MadelineProto/GroupCall/GroupCallState.html)




### <a name="leave"></a> `leave(): static`

Leave the conference call, without ending it for the other participants.



### <a name="discard"></a> `discard(): static`

End the conference call for everyone, if we created it, and leave it.
  
Only the creator of a conference may end it: for anyone else the server refuses and this simply  
{@see self::leave()}s the call.  



### <a name="getParticipants"></a> `getParticipants(): array<int, array{public_key: string, permissions: int, version: int}>`

Get the participants currently in the conference, keyed by their user id, each with their
Ed25519 `public_key`, `permissions` bits and protocol `version` from the shared-state chain.  



### <a name="getParticipant"></a> `getParticipant(mixed $participant): (array{public_key: string, permissions: int, version: int}|null)`

A participant of the conference by their id, username or peer, with their Ed25519 `public_key`,
`permissions` bits and protocol `version` from the shared-state chain, or null if not in it.  


Parameters:

* `$participant`: `mixed`   



### <a name="removeParticipant"></a> `removeParticipant(mixed ...$participants): static`

Remove participants from the conference and rekey for the remaining members, so the removed
members can no longer decrypt the call's media. Requires the `remove_users` permission.  


Parameters:

* `...$participants`: `mixed`   



### <a name="invite"></a> `invite(mixed ...$users): static`

Invite users to the conference call, ringing them.


Parameters:

* `...$users`: `mixed`   



### <a name="exportInvite"></a> `exportInvite(bool $canSelfUnmute = false): string`

The [conference link »](https://core.telegram.org/api/links#conference-links) of this conference
call, which anyone can use to join it.  


Parameters:

* `$canSelfUnmute`: `bool` Ignored: a conference has no admins, everyone may speak.  



### <a name="setTitle"></a> `setTitle(string $title): static`

Change the title of the conference call.


Parameters:

* `$title`: `string`   



### <a name="getVisualization"></a> `getVisualization(): (list<string>|null)`

The four [key verification emojis »](https://core.telegram.org/api/end-to-end/group-calls#verifying-the-key),
which every participant can compare to make sure nobody is in the middle.  
  
Verification (a commit-reveal exchange between all participants) runs automatically whenever  
the set of participants changes; this returns null until it completes for the current state.  



### <a name="sendMessage"></a> `sendMessage(string $message, (\danog\MadelineProto\ParseMode|null) $parseMode = NULL, (int|null) $paidStars = NULL, mixed $sendAs = NULL): static`

Send an end-to-end encrypted [in-call message »](https://core.telegram.org/api/end-to-end/group-calls#conference-in-call-messages)
to every participant of the conference.  


Parameters:

* `$message`: `string` The text; markup in `$parseMode` is converted to entities (bold, italic, underline, strikethrough, spoiler and custom emoji are supported).  
* `$parseMode`: `(\danog\MadelineProto\ParseMode|null)` Whether to parse HTML or Markdown markup in the text.  
* `$paidStars`: `(int|null)` Ignored: conference messages cannot carry donations.  
* `$sendAs`: `mixed` Ignored: conference messages are always sent as ourselves.  


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../../../danog/MadelineProto/ParseMode.html)




### <a name="sendReaction"></a> `sendReaction(string $emoji, (int|null) $customEmojiId = NULL): static`

Send an end-to-end encrypted [in-call reaction »](https://core.telegram.org/api/end-to-end/group-calls#conference-in-call-reactions).


Parameters:

* `$emoji`: `string` The emoji.  
* `$customEmojiId`: `(int|null)` The document id of a custom emoji to send instead, `$emoji` being its fallback.  



### <a name="setMessagesEnabled"></a> `setMessagesEnabled(bool $enabled): static`

Enable or disable in-call messages.


Parameters:

* `$enabled`: `bool`   



### <a name="muteParticipant"></a> `muteParticipant(mixed $participant, bool $muted = true): static`

Mute a participant for ourselves only (a conference has no admins).


Parameters:

* `$participant`: `mixed`   
* `$muted`: `bool`   



### <a name="setParticipantVolume"></a> `setParticipantVolume(mixed $participant, int $volume): static`

Set our local playback volume of a participant.


Parameters:

* `$participant`: `mixed`   
* `$volume`: `int` From 1 to 20000, where 10000 is 100%.  



### <a name="setVideoPaused"></a> `setVideoPaused(bool $paused): static`

Pause or resume our own video stream, telling the other participants to keep showing the last
frame rather than hiding it.  


Parameters:

* `$paused`: `bool`   



### <a name="setJoinMuted"></a> `setJoinMuted(bool $joinMuted): static`

Whether new participants join muted.


Parameters:

* `$joinMuted`: `bool`   



### <a name="resetInviteHash"></a> `resetInviteHash(): static`

Invalidate the conference link exported so far, so a new one is generated.



### <a name="isStreamMode"></a> `isStreamMode(): bool`

A conference is always received over WebRTC (its media is end-to-end encrypted): never in stream mode.



### <a name="isRtmpMode"></a> `isRtmpMode(): bool`

A conference has no RTMP publisher.



### <a name="isSharingScreen"></a> `isSharingScreen(): bool`

Whether a screen-share is currently being transmitted.



### <a name="enablePresentation"></a> `enablePresentation(): static`

Start sharing a screen: a second, end-to-end encrypted connection whose video is transmitted on
the {@see MediaDestination::Presentation} stream. Idempotent; requires the call to be joined.  



### <a name="disablePresentation"></a> `disablePresentation(): static`

Stop sharing the screen.



### <a name="setOutput"></a> `setOutput(\danog\MadelineProto\LocalFile|\danog\MadelineProto\LocalDirectory|\Amp\ByteStream\WritableStream $file, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): static`

Record conference call media, muxed into a Matroska file in pure PHP.
  
Only a {@see LocalDirectory} is accepted: it records every transmitting participant — or only the  
given `$participant` — as `<dir>/<userId>.<n>_<streams>.mkv` files, one per combination of the  
audio, camera video and screen share they send, each on or off at any time (see  
{@see Call::setOutput()}; participants that start transmitting later are picked up too). Our own  
media is never recorded. Every recording is plaintext — the frames are decrypted before they are  
muxed.  
  
Participants' frames are stored as-is, so the video tracks are whatever codec they send and the  
audio is OPUS; `$format` picks the {@see RecordingFormat::Mkv} (default) or {@see RecordingFormat::Webm}  
DocType, autodetected from a `.webm` extension. Audio-only OGG OPUS recordings are not supported.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\LocalDirectory|\Amp\ByteStream\WritableStream`   
* `$participant`: `mixed`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\LocalDirectory`: Indicates a local directory to write output into.](../../../../danog/MadelineProto/LocalDirectory.html)
* `\Amp\ByteStream\WritableStream`
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()}.](../../../../danog/MadelineProto/RecordingFormat.html)




### <a name="setMuted"></a> `setMuted(bool $muted = true): static`

Mute or unmute our own audio stream.


Parameters:

* `$muted`: `bool`   



### <a name="isMuted"></a> `isMuted(): bool`

Whether our own audio stream is muted.



### <a name="play"></a> `play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play a file, transmitting its audio and, if it carries a transmittable one, its video, all
end-to-end encrypted before it reaches the SFU.  
  
A WebM/Matroska file with VP8, VP9 or H.264 video has its video transmitted too; any other  
file (or a raw audio stream) is played as audio only. Frames are demuxed in pure PHP and sent  
as-is where possible, so no transcoding (and thus no FFI extension) is required for  
pre-encoded WebM/OGG-OPUS input.  


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
  
Will return a string with the object ID of the stream if we're currently playing a stream,  
otherwise returns the related LocalFile or RemoteUrl.  


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
