---
title: "danog\\MadelineProto\\Tgcalls\\E2E\\ConferenceCall: Controller for a Telegram end-to-end encrypted conference call"
description: "([end-to-end group calls](https://core.telegram.org/api/end-to-end/group-calls)).\n\nIt owns the two block subchains ({@see ConferenceChain} + {@see Verification}), turns the accepted\nblocks into media-encryption epochs, and drives a {@see GroupConnection} whose RTP frames are\nend-to-end encrypted by a {@see FrameCryptor} — the SFU only ever forwards ciphertext. It is both\nthe connection's owner and the cryptor's key provider.\n\nThis is the public object returned by {@see \\danog\\MadelineProto\\MTProto::createConferenceCall()}\nand {@see \\danog\\MadelineProto\\MTProto::joinConferenceCall()}; it implements the common\n{@see Call} media interface plus conference-specific controls (verification, encrypted messages).\n"
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

This is the public object returned by {@see \danog\MadelineProto\MTProto::createConferenceCall()}
and {@see \danog\MadelineProto\MTProto::joinConferenceCall()}; it implements the common
{@see Call} media interface plus conference-specific controls (verification, encrypted messages).


## Properties
* `$API`: `danog\MadelineProto\MTProto` 

## Method list:
* [`__construct(\danog\MadelineProto\MTProto $API)`](#__construct)
* [`resumeAfterRestart(): void`](#resumeAfterRestart)
* [`setCall(array $call): void`](#setCall)
* [`getInputCall(): array`](#getInputCall)
* [`isJoined(): bool`](#isJoined)
* [`isSharingScreen(): bool`](#isSharingScreen)
* [`activeEpochs(): array`](#activeEpochs)
* [`selfSeed(): string`](#selfSeed)
* [`publicKeyForSsrc(int $ssrc): ?string`](#publicKeyForSsrc)
* [`create(bool $muted = false): void`](#create)
* [`join(bool $muted = false): void`](#join)
* [`removeParticipant(int ...$userIds): void`](#removeParticipant)
* [`syncChain(int $subChainId): void`](#syncChain)
* [`enablePresentation(): void`](#enablePresentation)
* [`disablePresentation(): void`](#disablePresentation)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, \danog\MadelineProto\MediaDestination $dest = \danog\MadelineProto\MediaDestination::Camera): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`](#play)
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
* [`getParticipants(): array<int, array{public_key: string, permissions: int}>`](#getParticipants)
* [`startVerification(): void`](#startVerification)
* [`getEmojis(): (list<string>|null)`](#getEmojis)
* [`sendMessage(string $message): void`](#sendMessage)
* [`setParticipants(list<array{user_id: int, source: int, video: list<int>, presentation: list<int>, videoEndpoint: ?string, presentationEndpoint: ?string}> $participants): void`](#setParticipants)
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


### <a name="isJoined"></a> `isJoined(): bool`

Whether we are currently in the conference (joined and not left/forbidden).



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



### <a name="join"></a> `join(bool $muted = false): void`

Join an existing conference call: fetch the chain, add ourselves in a new block, and join with
that block.  


Parameters:

* `$muted`: `bool`   



### <a name="removeParticipant"></a> `removeParticipant(int ...$userIds): void`

Remove participants from the conference: build a block dropping them and rekeying for the
remaining members, then submit it with phone.deleteConferenceCallParticipants. Requires the  
`remove_users` permission. The removed members can no longer decrypt media once the new epoch  
takes over.  


Parameters:

* `...$userIds`: `int`   



### <a name="syncChain"></a> `syncChain(int $subChainId): void`

Fetch and apply every block of a subchain from our current offset until caught up.


Parameters:

* `$subChainId`: `int`   



### <a name="enablePresentation"></a> `enablePresentation(): void`

Start sharing a screen: a second WebRTC connection (phone.joinGroupCallPresentation) whose
video is end-to-end encrypted with the same conference keys, on its own packet channel so its  
sequence numbers never collide with the camera's. Idempotent.  



### <a name="disablePresentation"></a> `disablePresentation(): void`

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

Discard (leave) the conference call.



### <a name="leave"></a> `leave(): \danog\MadelineProto\Tgcalls\E2E\ConferenceCall`

Leave the conference, keeping it running for the other participants: stop the backstop poll and
stop receiving its updates.  



### <a name="getParticipants"></a> `getParticipants(): array<int, array{public_key: string, permissions: int}>`

The participants currently in the conference, keyed by user id, each with their Ed25519
`public_key` and `permissions` bits from the shared-state chain.  



### <a name="startVerification"></a> `startVerification(): void`

Begin (or restart) verification for the current chain head: broadcast our nonce commit, then
its reveal. All participants then converge on the same four emojis.  



### <a name="getEmojis"></a> `getEmojis(): (list<string>|null)`

The four verification emojis, or null until every participant's nonce has been revealed.



### <a name="sendMessage"></a> `sendMessage(string $message): void`

Send an end-to-end encrypted in-call message to every participant (channel 0), encrypted with
{@see CallPacket} for the current epochs.  


Parameters:

* `$message`: `string`   



### <a name="setParticipants"></a> `setParticipants(list<array{user_id: int, source: int, video: list<int>, presentation: list<int>, videoEndpoint: ?string, presentationEndpoint: ?string}> $participants): void`

Update the SSRC -> user id map from the group call participant list, so incoming media can be
attributed to a sender's public key, and tell the connection which sources to receive.  


Parameters:

* `$participants`: `list<array{user_id: int, source: int, video: list<int>, presentation: list<int>, videoEndpoint: ?string, presentationEndpoint: ?string}>`   



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
