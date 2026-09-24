---
title: "danog\\MadelineProto\\Tgcalls\\E2E\\ConferenceCall: Controller for a Telegram end-to-end encrypted conference call"
description: "([end-to-end group calls](https://core.telegram.org/api/end-to-end/group-calls)).\n\nIt owns the two block subchains ({@see ConferenceChain} + {@see Verification}), turns the accepted\nblocks into media-encryption epochs, and drives a {@see GroupConnection} whose RTP frames are\nend-to-end encrypted by a {@see FrameCryptor} — the SFU only ever forwards ciphertext. It is both\nthe connection's owner and the cryptor's key provider.\n\nThis is the internal controller; the public handle library users receive from\n{@see \\danog\\MadelineProto\\MTProto::createConferenceCall()} and\n{@see \\danog\\MadelineProto\\MTProto::joinConferenceCall()} is the {@see ConferenceCallUpdate}\nreturned by {@see self::getPublic()}, which delegates back here by call id. The controller\nimplements the common {@see Call} media interface plus conference-specific controls (verification,\nencrypted messages).\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Tgcalls\E2E\ConferenceCall`
[Back to index](../../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Controller for a Telegram end-to-end encrypted conference call  

([end-to-end group calls](https://core.telegram.org/api/end-to-end/group-calls)).

It owns the two block subchains ({@see ConferenceChain} + {@see Verification}), turns the accepted
blocks into media-encryption epochs, and drives a {@see GroupConnection} whose RTP frames are
end-to-end encrypted by a {@see FrameCryptor} — the SFU only ever forwards ciphertext. It is both
the connection's owner and the cryptor's key provider.

This is the internal controller; the public handle library users receive from
{@see \danog\MadelineProto\MTProto::createConferenceCall()} and
{@see \danog\MadelineProto\MTProto::joinConferenceCall()} is the {@see ConferenceCallUpdate}
returned by {@see self::getPublic()}, which delegates back here by call id. The controller
implements the common {@see Call} media interface plus conference-specific controls (verification,
encrypted messages).


## Properties
* `$API`: `danog\MadelineProto\MTProto` 

## Method list:
* [`__construct(\danog\MadelineProto\MTProto $API)`](#__construct)
* [`resumeAfterRestart(): void`](#resumeAfterRestart)
* [`setCall(array $call): void`](#setCall)
* [`getInputCall(): array`](#getInputCall)
* [`getPublic(): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`](#getPublic)
* [`isJoined(): bool`](#isJoined)
* [`isCallEnded(): bool`](#isCallEnded)
* [`getCallState(): \danog\MadelineProto\EventHandler\Calls\GroupCallState`](#getCallState)
* [`activeEpochs(): array`](#activeEpochs)
* [`selfSeed(): string`](#selfSeed)
* [`publicKeyForSsrc(int $ssrc): ?string`](#publicKeyForSsrc)
* [`create(bool $muted = false): void`](#create)
* [`join(bool $muted = false): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#join)
* [`editParticipant(array|string|int $participant, ?bool $muted = NULL, ?int $volume = NULL, ?bool $videoPaused = NULL): void`](#editParticipant)
* [`toggleSettings(?bool $joinMuted = NULL, bool $resetInviteHash = false, ?bool $messagesEnabled = NULL): void`](#toggleSettings)
* [`invite(string|int ...$users): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#invite)
* [`exportInvite(bool $canSelfUnmute = false): string`](#exportInvite)
* [`removeParticipant(string|int ...$participants): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#removeParticipant)
* [`syncChain(int $subChainId): void`](#syncChain)
* [`then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#then)
* [`discard(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#discard)
* [`leave(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#leave)
* [`getParticipants(): array<int, \danog\MadelineProto\EventHandler\Calls\ConferenceCallParticipant>`](#getParticipants)
* [`getVisualization(): (list<string>|null)`](#getVisualization)
* [`sendMessage(string $message, ?\danog\MadelineProto\ParseMode $parseMode = NULL, ?int $paidStars = NULL, mixed $sendAs = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#sendMessage)
* [`sendReaction(string $emoji, ?int $customEmojiId = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#sendReaction)
* [`setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, ?StreamMask $streams = NULL): StreamMask`](#setOutput)
* [`setOutputFolder(\danog\MadelineProto\LocalDirectory $dir, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#setOutputFolder)
* [`getChain(): \danog\MadelineProto\Tgcalls\E2E\ConferenceChain`](#getChain)
* [`log(string $message, int $level = \danog\MadelineProto\Logger::NOTICE): void`](#log)
* [`onIncomingSource(int $source): void`](#onIncomingSource)
* [`onConnectionFailed(): void`](#onConnectionFailed)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#play)
* [`playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#playBlocking)
* [`playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`](#playOnHold)
* [`skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#skip)
* [`stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#stop)
* [`pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#pause)
* [`resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`](#resume)
* [`getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|string|null`](#getCurrent)
* [`isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`](#isPaused)
* [`enablePresentation(): static`](#enablePresentation)
* [`disablePresentation(): static`](#disablePresentation)
* [`isSharingScreen(): bool`](#isSharingScreen)
* [`setMuted(bool $muted = true): static`](#setMuted)
* [`isMuted(): bool`](#isMuted)
* [`setTitle(string $title): static`](#setTitle)

## Methods:
### <a name="__construct"></a> `__construct(\danog\MadelineProto\MTProto $API)`




Parameters:

* `$API`: `\danog\MadelineProto\MTProto`   


#### See also: 
* `\danog\MadelineProto\MTProto`




### <a name="resumeAfterRestart"></a> `resumeAfterRestart(): void`

Resume the conference after the process restarted: reopen the media connection, re-register for
push updates, restart the backstop poll and catch up on any blocks missed while stopped. Named  
to avoid clashing with the {@see Call} playback {@see self::resume()}.  



### <a name="setCall"></a> `setCall(array $call): void`

Point this controller at an existing conference (its groupCall), before joining it.


Parameters:

* `$call`: `array`   



### <a name="getInputCall"></a> `getInputCall(): array`




Return value: The inputGroupCall, once the conference exists.


### <a name="getPublic"></a> `getPublic(): \danog\MadelineProto\EventHandler\Calls\ConferenceCall`

The public {@see ConferenceCallUpdate} handle for this conference, built lazily once the call
exists. This is the object handed to library users; it delegates every operation back to this  
controller by call id.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\ConferenceCall`: This update represents a Telegram [end-to-end encrypted conference call »](https://core.telegram.org/api/end-to-end/group-calls).](../../../../danog/MadelineProto/EventHandler/Calls/ConferenceCall.html)




### <a name="isJoined"></a> `isJoined(): bool`

Whether we are currently in the conference (joined and not left/forbidden).



### <a name="isCallEnded"></a> `isCallEnded(): bool`

Whether we left (or discarded) the conference for good: the playback machinery stops then, but
not while we are merely between a drop and the automatic re-join.  



### <a name="getCallState"></a> `getCallState(): \danog\MadelineProto\EventHandler\Calls\GroupCallState`

Get the state of the conference call.


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\GroupCallState`: State of a group call we are interacting with.](../../../../danog/MadelineProto/EventHandler/Calls/GroupCallState.html)




### <a name="activeEpochs"></a> `activeEpochs(): array`





### <a name="selfSeed"></a> `selfSeed(): string`





### <a name="publicKeyForSsrc"></a> `publicKeyForSsrc(int $ssrc): ?string`




Parameters:

* `$ssrc`: `int`   



### <a name="create"></a> `create(bool $muted = false): void`

Create a brand-new conference call with ourselves as the sole participant and join it. Returns
the raw `phone.groupCall` this controller now drives.  


Parameters:

* `$muted`: `bool`   



### <a name="join"></a> `join(bool $muted = false): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Join an existing conference call: fetch the chain, add ourselves in a new block, and join with
that block.  


Parameters:

* `$muted`: `bool`   



### <a name="editParticipant"></a> `editParticipant(array|string|int $participant, ?bool $muted = NULL, ?int $volume = NULL, ?bool $videoPaused = NULL): void`

Change a participant's state (phone.editGroupCallParticipant): mute them for ourselves, set our
playback volume of them, or pause/resume our own video.  


Parameters:

* `$participant`: `array|string|int`   
* `$muted`: `?bool`   
* `$volume`: `?int`   
* `$videoPaused`: `?bool`   



### <a name="toggleSettings"></a> `toggleSettings(?bool $joinMuted = NULL, bool $resetInviteHash = false, ?bool $messagesEnabled = NULL): void`

Change the conference's settings (phone.toggleGroupCallSettings): whether new members join
muted, whether in-call messages are enabled, or invalidate its conference link.  


Parameters:

* `$joinMuted`: `?bool`   
* `$resetInviteHash`: `bool`   
* `$messagesEnabled`: `?bool`   



### <a name="invite"></a> `invite(string|int ...$users): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Invite users to the conference call (phone.inviteConferenceCallParticipant), ringing them; once
they accept they add themselves to the chain with their own self-join block.  


Parameters:

* `...$users`: `string|int`   



### <a name="exportInvite"></a> `exportInvite(bool $canSelfUnmute = false): string`

The [conference link »](https://core.telegram.org/api/links#conference-links) of the call: it is
created with the call and carried by its groupCall (`invite_link`), so, like official clients, we  
read it from there rather than exporting one.  


Parameters:

* `$canSelfUnmute`: `bool`   



### <a name="removeParticipant"></a> `removeParticipant(string|int ...$participants): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Remove participants from the conference: build a block dropping them and rekeying for the
remaining members, then submit it with phone.deleteConferenceCallParticipants. Requires the  
`remove_users` permission. The removed members can no longer decrypt media once the new epoch  
takes over.  


Parameters:

* `...$participants`: `string|int`   



### <a name="syncChain"></a> `syncChain(int $subChainId): void`

Fetch and apply every block of a subchain from our current offset until caught up.


Parameters:

* `$subChainId`: `int`   



### <a name="then"></a> `then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`




Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="discard"></a> `discard(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

End the conference for everyone (phone.discardGroupCall, allowed to its creator only) and leave
it; if the server refuses, just leave.  



### <a name="leave"></a> `leave(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Leave the conference, keeping it running for the other participants: stop the backstop poll and
stop receiving its updates.  



### <a name="getParticipants"></a> `getParticipants(): array<int, \danog\MadelineProto\EventHandler\Calls\ConferenceCallParticipant>`

The participants currently in the conference, keyed by user id, each with their Ed25519
public key, permission bits and protocol version from the shared-state chain.  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Calls\ConferenceCallParticipant`: A participant of an end-to-end encrypted {@see ConferenceCall}, as reconstructed from the](../../../../danog/MadelineProto/EventHandler/Calls/ConferenceCallParticipant.html)




### <a name="getVisualization"></a> `getVisualization(): (list<string>|null)`

The four verification emojis of the current chain head, or null until every member has committed
and revealed their nonce for it.  



### <a name="sendMessage"></a> `sendMessage(string $message, ?\danog\MadelineProto\ParseMode $parseMode = NULL, ?int $paidStars = NULL, mixed $sendAs = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Send an end-to-end encrypted in-call message to every participant: a `groupCallMessage` JSON
document, as [the protocol](https://core.telegram.org/api/end-to-end/group-calls#in-call-messages)  
defines, encrypted with {@see CallPacket} on channel 0 for the current epochs.  


Parameters:

* `$message`: `string`   
* `$parseMode`: `?\danog\MadelineProto\ParseMode`   
* `$paidStars`: `?int`   
* `$sendAs`: `mixed`   


#### See also: 
* [`\danog\MadelineProto\ParseMode`: Indicates a parsing mode for text.](../../../../danog/MadelineProto/ParseMode.html)




### <a name="sendReaction"></a> `sendReaction(string $emoji, ?int $customEmojiId = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Send an end-to-end encrypted in-call reaction: a single emoji, or a custom emoji with `$emoji`
as its fallback.  


Parameters:

* `$emoji`: `string`   
* `$customEmojiId`: `?int`   



### <a name="setOutput"></a> `setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL, ?StreamMask $streams = NULL): StreamMask`

Record one participant's (decrypted) media into a single file (or stream) with a fixed set of
tracks, see {@see GroupMediaTrait::recordParticipant()}.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream`   
* `$participant`: `string|int|null`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   
* `$streams`: `?StreamMask` The {@see CallStream} flags to record, or null for every available one.  


Return value: The streams the participant currently sends, as {@see CallStream} flags.

#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* `\Amp\ByteStream\WritableStream`
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../../../danog/MadelineProto/RecordingFormat.html)
* `StreamMask`




### <a name="setOutputFolder"></a> `setOutputFolder(\danog\MadelineProto\LocalDirectory $dir, string|int|null $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Record the conference (decrypted) into a directory, as numbered series of Matroska files, one
per participant, see {@see GroupMediaTrait::recordFolder()}.  


Parameters:

* `$dir`: `\danog\MadelineProto\LocalDirectory`   
* `$participant`: `string|int|null`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   


#### See also: 
* [`\danog\MadelineProto\LocalDirectory`: Indicates a local directory to write output into.](../../../../danog/MadelineProto/LocalDirectory.html)
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()} and {@see Call::setOutputFolder()}.](../../../../danog/MadelineProto/RecordingFormat.html)




### <a name="getChain"></a> `getChain(): \danog\MadelineProto\Tgcalls\E2E\ConferenceChain`




#### See also: 
* `\danog\MadelineProto\Tgcalls\E2E\ConferenceChain`




### <a name="log"></a> `log(string $message, int $level = \danog\MadelineProto\Logger::NOTICE): void`




Parameters:

* `$message`: `string`   
* `$level`: `int`   



### <a name="onIncomingSource"></a> `onIncomingSource(int $source): void`




Parameters:

* `$source`: `int`   



### <a name="onConnectionFailed"></a> `onConnectionFailed(): void`





### <a name="play"></a> `play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play a file, transmitting its audio and, if it carries a transmittable one, its video.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="playBlocking"></a> `playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Play a file, blocking until it has finished playing if a stream was passed.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="playOnHold"></a> `playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): static`

Set the files to play, on loop, while the given stream's main playlist is empty.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="skip"></a> `skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Skip to the next file in the playlist.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="stop"></a> `stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Stop playing all files, clearing the main and the hold playlist; stopping the presentation
stops sharing the screen.  


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="pause"></a> `pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Pause playback of the current file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="resume"></a> `resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): static`

Resume playback of the current file.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="getCurrent"></a> `getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|string|null`

The file or stream currently being played, if any.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)




### <a name="isPaused"></a> `isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`

Whether playback of the current file is paused.


Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="enablePresentation"></a> `enablePresentation(): static`

Start the separate screen-share connection (phone.joinGroupCallPresentation) if it is not up
yet. The screen-share is a fully separate WebRTC connection with its own SSRC and transport;  
see https://core.telegram.org/api/group-calls. Idempotent.  



### <a name="disablePresentation"></a> `disablePresentation(): static`

Stop sharing the screen: tear down the presentation connection and leave it server-side.



### <a name="isSharingScreen"></a> `isSharingScreen(): bool`

Whether a screen-share is currently being transmitted.



### <a name="setMuted"></a> `setMuted(bool $muted = true): static`

Mute or unmute ourselves.


Parameters:

* `$muted`: `bool`   



### <a name="isMuted"></a> `isMuted(): bool`

Whether we are muted.



### <a name="setTitle"></a> `setTitle(string $title): static`

Change the title of the call.


Parameters:

* `$title`: `string`   



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
