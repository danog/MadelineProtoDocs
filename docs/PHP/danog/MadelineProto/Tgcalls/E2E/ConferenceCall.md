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
* [`getCallState(): \danog\MadelineProto\GroupCall\GroupCallState`](#getCallState)
* [`isSharingScreen(): bool`](#isSharingScreen)
* [`activeEpochs(): array`](#activeEpochs)
* [`selfSeed(): string`](#selfSeed)
* [`publicKeyForSsrc(int $ssrc): ?string`](#publicKeyForSsrc)
* [`create(bool $muted = false): void`](#create)
* [`join(bool $muted = false): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#join)
* [`editParticipant(mixed $participant, ?bool $muted = NULL, ?int $volume = NULL, ?bool $videoPaused = NULL): void`](#editParticipant)
* [`toggleSettings(?bool $joinMuted = NULL, bool $resetInviteHash = false, ?bool $messagesEnabled = NULL): void`](#toggleSettings)
* [`setTitle(string $title): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#setTitle)
* [`invite(mixed ...$users): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#invite)
* [`exportInvite(bool $canSelfUnmute = false): string`](#exportInvite)
* [`removeParticipant(mixed ...$participants): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#removeParticipant)
* [`syncChain(int $subChainId): void`](#syncChain)
* [`enablePresentation(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#enablePresentation)
* [`disablePresentation(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#disablePresentation)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#play)
* [`playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#playBlocking)
* [`then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#then)
* [`playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#playOnHold)
* [`skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#skip)
* [`stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#stop)
* [`pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#pause)
* [`isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`](#isPaused)
* [`resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#resume)
* [`getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|string|null`](#getCurrent)
* [`setMuted(bool $muted = true): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#setMuted)
* [`isMuted(): bool`](#isMuted)
* [`discard(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#discard)
* [`leave(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#leave)
* [`getParticipants(): array<int, array{public_key: string, permissions: int, version: int}>`](#getParticipants)
* [`getVisualization(): (list<string>|null)`](#getVisualization)
* [`sendMessage(string $message, ?\danog\MadelineProto\ParseMode $parseMode = NULL, ?int $paidStars = NULL, mixed $sendAs = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#sendMessage)
* [`sendReaction(string $emoji, ?int $customEmojiId = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#sendReaction)
* [`setOutput(\danog\MadelineProto\LocalFile|\danog\MadelineProto\LocalDirectory|\Amp\ByteStream\WritableStream $file, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#setOutput)
* [`getChain(): \danog\MadelineProto\Tgcalls\E2E\ConferenceChain`](#getChain)
* [`log(string $message, int $level = \danog\MadelineProto\Logger::NOTICE): void`](#log)
* [`onIncomingSource(int $source): void`](#onIncomingSource)
* [`onConnectionFailed(): void`](#onConnectionFailed)
* [`setVideoStopped(bool $stopped): void`](#setVideoStopped)
* [`setPresentationPaused(bool $paused): void`](#setPresentationPaused)

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



### <a name="getCallState"></a> `getCallState(): \danog\MadelineProto\GroupCall\GroupCallState`

Get the state of the conference call.


#### See also: 
* [`\danog\MadelineProto\GroupCall\GroupCallState`: State of a group call we are interacting with.](../../../../danog/MadelineProto/GroupCall/GroupCallState.html)




### <a name="isSharingScreen"></a> `isSharingScreen(): bool`

Whether a screen-share is currently being transmitted.



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



### <a name="editParticipant"></a> `editParticipant(mixed $participant, ?bool $muted = NULL, ?int $volume = NULL, ?bool $videoPaused = NULL): void`

Change a participant's state (phone.editGroupCallParticipant): mute them for ourselves, set our
playback volume of them, or pause/resume our own video.  


Parameters:

* `$participant`: `mixed`   
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



### <a name="setTitle"></a> `setTitle(string $title): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Change the title of the conference call.


Parameters:

* `$title`: `string`   



### <a name="invite"></a> `invite(mixed ...$users): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Invite users to the conference call (phone.inviteConferenceCallParticipant), ringing them; once
they accept they add themselves to the chain with their own self-join block.  


Parameters:

* `...$users`: `mixed`   



### <a name="exportInvite"></a> `exportInvite(bool $canSelfUnmute = false): string`

The [conference link »](https://core.telegram.org/api/links#conference-links) of the call: it is
created with the call and carried by its groupCall (`invite_link`), so, like official clients, we  
read it from there rather than exporting one.  


Parameters:

* `$canSelfUnmute`: `bool`   



### <a name="removeParticipant"></a> `removeParticipant(mixed ...$participants): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Remove participants from the conference: build a block dropping them and rekeying for the
remaining members, then submit it with phone.deleteConferenceCallParticipants. Requires the  
`remove_users` permission. The removed members can no longer decrypt media once the new epoch  
takes over.  


Parameters:

* `...$participants`: `mixed`   



### <a name="syncChain"></a> `syncChain(int $subChainId): void`

Fetch and apply every block of a subchain from our current offset until caught up.


Parameters:

* `$subChainId`: `int`   



### <a name="enablePresentation"></a> `enablePresentation(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Start sharing a screen: a second WebRTC connection (phone.joinGroupCallPresentation) whose
video is end-to-end encrypted with the same conference keys, on its own packet channel so its  
sequence numbers never collide with the camera's. Idempotent.  



### <a name="disablePresentation"></a> `disablePresentation(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Stop sharing the screen: tear down the presentation connection and tell the server.



### <a name="play"></a> `play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`




Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="playBlocking"></a> `playBlocking(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Play a file, blocking until it has finished playing if a stream is provided.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="then"></a> `then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`




Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="playOnHold"></a> `playOnHold(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera, \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`




Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   
* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="skip"></a> `skip(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`




Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="stop"></a> `stop(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`




Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="pause"></a> `pause(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`




Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="isPaused"></a> `isPaused(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): bool`




Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="resume"></a> `resume(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`




Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)




### <a name="getCurrent"></a> `getCurrent(\danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|string|null`




Parameters:

* `$dest`: `\danog\MadelineProto\MediaDestination`   


#### See also: 
* [`\danog\MadelineProto\MediaDestination`: Which media stream of a call a playback or recording operation targets.](../../../../danog/MadelineProto/MediaDestination.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../../../danog/MadelineProto/RemoteUrl.html)




### <a name="setMuted"></a> `setMuted(bool $muted = true): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`




Parameters:

* `$muted`: `bool`   



### <a name="isMuted"></a> `isMuted(): bool`





### <a name="discard"></a> `discard(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

End the conference for everyone (phone.discardGroupCall, allowed to its creator only) and leave
it; if the server refuses, just leave.  



### <a name="leave"></a> `leave(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Leave the conference, keeping it running for the other participants: stop the backstop poll and
stop receiving its updates.  



### <a name="getParticipants"></a> `getParticipants(): array<int, array{public_key: string, permissions: int, version: int}>`

The participants currently in the conference, keyed by user id, each with their Ed25519
`public_key` and `permissions` bits from the shared-state chain.  



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



### <a name="setOutput"></a> `setOutput(\danog\MadelineProto\LocalFile|\danog\MadelineProto\LocalDirectory|\Amp\ByteStream\WritableStream $file, mixed $participant = NULL, ?\danog\MadelineProto\RecordingFormat $format = NULL): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Record conference call media (all end-to-end encrypted; the SFU only ever sees ciphertext, but
incoming frames are decrypted before they are muxed, so recordings are plaintext).  
  
Only a {@see LocalDirectory} is accepted: every *transmitting* participant — or only the given  
`$participant` — is recorded as `<dir>/<userId>.<n>_<streams>.mkv` files, one per combination of  
the audio, camera video and screen share they send, which they can turn on and off at any time  
(see {@see \danog\MadelineProto\EventHandler\Call::setOutput()}). Participants that start  
transmitting later are picked up too; our own media is never recorded.  
  
`$format` picks the Matroska DocType ({@see RecordingFormat::matroskaFor()}); OGG OPUS is not supported.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\LocalDirectory|\Amp\ByteStream\WritableStream`   
* `$participant`: `mixed`   
* `$format`: `?\danog\MadelineProto\RecordingFormat`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\LocalDirectory`: Indicates a local directory to write output into.](../../../../danog/MadelineProto/LocalDirectory.html)
* `\Amp\ByteStream\WritableStream`
* [`\danog\MadelineProto\RecordingFormat`: Container format of a call recording, as passed to {@see Call::setOutput()}.](../../../../danog/MadelineProto/RecordingFormat.html)




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





### <a name="setVideoStopped"></a> `setVideoStopped(bool $stopped): void`




Parameters:

* `$stopped`: `bool`   



### <a name="setPresentationPaused"></a> `setPresentationPaused(bool $paused): void`




Parameters:

* `$paused`: `bool`   



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
