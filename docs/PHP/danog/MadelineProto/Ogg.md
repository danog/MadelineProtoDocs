---
title: "danog\\MadelineProto\\Ogg: Async OGG stream reader and writer."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Ogg`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
> Author: Charles-Édouard Coste <contact@ccoste.fr>  
  

Async OGG stream reader and writer.  




## Constants
* `danog\MadelineProto\Ogg::CONTINUATION`: 

* `danog\MadelineProto\Ogg::BOS`: 

* `danog\MadelineProto\Ogg::EOS`: 

* `danog\MadelineProto\Ogg::STATE_READ_HEADER`: 

* `danog\MadelineProto\Ogg::STATE_READ_COMMENT`: 

* `danog\MadelineProto\Ogg::STATE_STREAMING`: 

* `danog\MadelineProto\Ogg::STATE_END`: 

## Properties
* `$opusPackets`: `iterable<string>` 
* `$vendorString`: `string` 
* `$comments`: `list<string>` 

## Method list:
* [`__construct(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL)`](#__construct)
* [`validate(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, ?\Amp\Cancellation $cancellation = NULL): void`](#validate)
* [`convert(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $in, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $oggOut, ?\Amp\Cancellation $cancellation = NULL): void`](#convert)
* [`validateOgg(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $f): void`](#validateogg)
* [`convertWav(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $wavIn, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $oggOut, ?\Amp\Cancellation $cancellation = NULL): void`](#convertwav)

## Methods:
### `__construct(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL)`

Constructor.


Parameters:

* `$stream`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\Cancellation`




### `validate(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $file, ?\Amp\Cancellation $cancellation = NULL): void`

Validate that the specified file, URL or stream is a valid VoIP OGG OPUS file.


Parameters:

* `$file`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\Cancellation`




### `convert(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $in, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $oggOut, ?\Amp\Cancellation $cancellation = NULL): void`

Converts a file, URL, or stream of any format (including video) into an OGG audio stream suitable for consumption by MadelineProto's VoIP implementation.


Parameters:

* `$in`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream` The input file, URL or stream.  
* `$oggOut`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream` The output file or stream.  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\ByteStream\WritableStream`
* `\Amp\Cancellation`




### `validateOgg(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $f): void`

Validate that the specified OGG OPUS file can be played directly by MadelineProto, without doing any conversion.


Parameters:

* `$f`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`




### `convertWav(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $wavIn, \danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream $oggOut, ?\Amp\Cancellation $cancellation = NULL): void`

Converts a file, URL, or stream in WAV format @ 48khz into an OGG audio stream suitable for consumption by MadelineProto's VoIP implementation.


Parameters:

* `$wavIn`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream` The input file, URL or stream.  
* `$oggOut`: `\danog\MadelineProto\LocalFile|\Amp\ByteStream\WritableStream` The output file or stream.  
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\ByteStream\WritableStream`
* `\Amp\Cancellation`




---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
