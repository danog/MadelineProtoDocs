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
* `$video`: `bool` Whether this is a video call.
* `$otherID`: `int` ID of the other user in the call
* `$date`: `int` When was the call created
* `$discardReason`: `?danog\MadelineProto\VoIP\DiscardReason` Why the call was discarded, if it was.
* `$conferenceSlug`: `?string` If the call was upgraded to a [conference call »](https://core.telegram.org/api/group-calls#conference-calls),
the [conference deep link »](https://core.telegram.org/api/links#conference-links) slug of the new conference.

Conference calls are end-to-end encrypted and cannot be joined by MadelineProto yet.

## Method list:
* [`accept(): \danog\MadelineProto\VoIP`](#accept)
* [`discard(\danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<1, 5> $rating = NULL, string $comment = NULL): \danog\MadelineProto\VoIP`](#discard)
* [`getVisualization(): ?list{string, string, string, string}`](#getVisualization)
* [`play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): \danog\MadelineProto\VoIP`](#play)
* [`setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file): \danog\MadelineProto\VoIP`](#setOutput)
* [`then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): \danog\MadelineProto\VoIP`](#then)
* [`playVideo(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): \danog\MadelineProto\VoIP`](#playVideo)
* [`stopVideo(): \danog\MadelineProto\VoIP`](#stopVideo)
* [`skip(): \danog\MadelineProto\VoIP`](#skip)
* [`stop(): \danog\MadelineProto\VoIP`](#stop)
* [`pause(): \danog\MadelineProto\VoIP`](#pause)
* [`isPaused(): boolean`](#isPaused)
* [`resume(): \danog\MadelineProto\VoIP`](#resume)
* [`playOnHold(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): \danog\MadelineProto\VoIP`](#playOnHold)
* [`getCurrent(): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`](#getCurrent)
* [`setMuted(bool $muted = true): \danog\MadelineProto\VoIP`](#setMuted)
* [`isMuted(): bool`](#isMuted)
* [`getRemoteMediaState(): ?\danog\MadelineProto\VoIP\MediaState`](#getRemoteMediaState)
* [`getCallState(): \danog\MadelineProto\VoIP\CallState`](#getCallState)

## Methods:
### <a name="accept"></a> `accept(): \danog\MadelineProto\VoIP`

Accept call.



### <a name="discard"></a> `discard(\danog\MadelineProto\VoIP\DiscardReason $reason = \danog\MadelineProto\VoIP\DiscardReason::HANGUP, int<1, 5> $rating = NULL, string $comment = NULL): \danog\MadelineProto\VoIP`

Discard call.


Parameters:

* `$reason`: `\danog\MadelineProto\VoIP\DiscardReason`   
* `$rating`: `int<1, 5>` Call rating in stars  
* `$comment`: `string` Additional comment on call quality.  


#### See also: 
* [`\danog\MadelineProto\VoIP\DiscardReason`: Why was the call discarded?](../../danog/MadelineProto/VoIP/DiscardReason.html)




### <a name="getVisualization"></a> `getVisualization(): ?list{string, string, string, string}`

Get call emojis (will return null if the call is not inited yet).



### <a name="play"></a> `play(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): \danog\MadelineProto\VoIP`

Play file.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="setOutput"></a> `setOutput(\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $file): \danog\MadelineProto\VoIP`

Set output file or stream for incoming OPUS audio packets.
  
Will write an OGG OPUS stream to the specified file or stream.  


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* `\Amp\ByteStream\WritableStream`




### <a name="then"></a> `then(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): \danog\MadelineProto\VoIP`

Play file.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="playVideo"></a> `playVideo(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file): \danog\MadelineProto\VoIP`

Play the VP8 video and OPUS audio of a WebM file.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="stopVideo"></a> `stopVideo(): \danog\MadelineProto\VoIP`

Stop transmitting video.



### <a name="skip"></a> `skip(): \danog\MadelineProto\VoIP`

When called, skips to the next file in the playlist.



### <a name="stop"></a> `stop(): \danog\MadelineProto\VoIP`

Stops playing all files, clears the main and the hold playlist.



### <a name="pause"></a> `pause(): \danog\MadelineProto\VoIP`

Pauses the currently playing file.



### <a name="isPaused"></a> `isPaused(): boolean`

Whether the currently playing file is paused.



### <a name="resume"></a> `resume(): \danog\MadelineProto\VoIP`

Resumes the currently playing file.



### <a name="playOnHold"></a> `playOnHold(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream ...$files): \danog\MadelineProto\VoIP`

Files to play on hold.


Parameters:

* `...$files`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### <a name="getCurrent"></a> `getCurrent(): \danog\MadelineProto\RemoteUrl|\danog\MadelineProto\LocalFile|string|null`

Get the file that is currently being played.
  
Will return a string with the object ID of the stream if we're currently playing a stream, otherwise returns the related LocalFile or RemoteUrl.  


#### See also: 
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)




### <a name="setMuted"></a> `setMuted(bool $muted = true): \danog\MadelineProto\VoIP`

Mute or unmute our own audio stream.


Parameters:

* `$muted`: `bool`   



### <a name="isMuted"></a> `isMuted(): bool`

Whether our own audio stream is muted.



### <a name="getRemoteMediaState"></a> `getRemoteMediaState(): ?\danog\MadelineProto\VoIP\MediaState`

Get the media state of the other party, as reported by their client.
  
Will return null if the call is not connected yet.  


#### See also: 
* [`\danog\MadelineProto\VoIP\MediaState`: The media state of the other party of a one-to-one call, as reported by its `MediaState`](../../danog/MadelineProto/VoIP/MediaState.html)




### <a name="getCallState"></a> `getCallState(): \danog\MadelineProto\VoIP\CallState`

Get call state.


#### See also: 
* [\danog\MadelineProto\VoIP\CallState](../../danog/MadelineProto/VoIP/CallState.html)




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
