---
title: "danog\\MadelineProto\\VoIP: This update represents a VoIP Telegram call."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\VoIP`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

This update represents a VoIP Telegram call.  



## Properties
* `$callID`: `int` Phone call ID
* `$outgoing`: `bool` Whether the call is an outgoing call
* `$otherID`: `int` ID of the other user in the call
* `$date`: `int` When was the call created

## Method list:
* [`accept(): self`](#accept-self)
* [`discard(\danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<\1, \5> $rating = NULL, string $comment = NULL): self`](#discard-danog-madelineproto-voip-discardreason-reason-danog-madelineproto-voip-discardreason-hangup-int-1-5-rating-null-string-comment-null-self)
* [`getVisualization(): ?array{0: \: string, 1: \: string, 2: \: string, 3: \: string}`](#getvisualization-array-0-string-1-string-2-string-3-string)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): self`](#play-danog-madelineproto-localfile-danog-madelineproto-remoteurl-amp-bytestream-readablestream-file-self)
* [`then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): self`](#then-danog-madelineproto-localfile-danog-madelineproto-remoteurl-amp-bytestream-readablestream-file-self)
* [`skip(): self`](#skip-self)
* [`stop(): self`](#stop-self)
* [`playOnHold(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): self`](#playonhold-danog-madelineproto-localfile-danog-madelineproto-remoteurl-amp-bytestream-readablestream-files-self)
* [`getCurrent(): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#getcurrent-danog-madelineproto-remoteurl-danog-madelineproto-localfile-string-null)
* [`getCallState(): \danog\MadelineProto\VoIP\CallState`](#getcallstate-danog-madelineproto-voip-callstate)

## Methods:
### `accept(): self`

Accept call.



### `discard(\danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<\1, \5> $rating = NULL, string $comment = NULL): self`

Discard call.


Parameters:

* `$reason`: `\danog\MadelineProto\VoIP\DiscardReason`   
* `$rating`: `int<\1, \5>` Call rating in stars  
* `$comment`: `string` Additional comment on call quality.  


#### See also: 
* [`\danog\MadelineProto\VoIP\DiscardReason`: Why was the call discarded?](../../danog/MadelineProto/VoIP/DiscardReason.html)




### `getVisualization(): ?array{0: \: string, 1: \: string, 2: \: string, 3: \: string}`

Get call emojis (will return null if the call is not inited yet).



### `play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): self`

Play file.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### `then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): self`

Play file.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### `skip(): self`

When called, skips to the next file in the playlist.



### `stop(): self`

Stops playing all files, clears the main and the hold playlist.



### `playOnHold(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): self`

Files to play on hold.


Parameters:

* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### `getCurrent(): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

Get the file that is currently being played.
Will return a string with the object ID of the stream if we're currently playing a stream, otherwise returns the related LocalFile or RemoteUrl.

#### See also: 
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)




### `getCallState(): \danog\MadelineProto\VoIP\CallState`

Get call state.


#### See also: 
* [\danog\MadelineProto\VoIP\CallState](../../danog/MadelineProto/VoIP/CallState.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
