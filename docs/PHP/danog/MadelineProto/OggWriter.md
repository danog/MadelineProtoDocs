---
title: "danog\\MadelineProto\\OggWriter: Async OGG stream writer."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\OggWriter`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Async OGG stream writer.  



## Properties
* `$streamId`: `int` 

## Method list:
* [`__construct(\Amp\ByteStream\WritableStream $out, ?int $streamId = NULL)`](#__construct-amp-bytestream-writablestream-out-int-streamid-null)
* [`writeHeader(int $channels, int $sampleRate, string $opusVersion): void`](#writeheader-int-channels-int-samplerate-string-opusversion-void)
* [`writeChunk(string $chunk, int $granuleDiff, bool $eos): void`](#writechunk-string-chunk-int-granulediff-bool-eos-void)

## Methods:
### `__construct(\Amp\ByteStream\WritableStream $out, ?int $streamId = NULL)`

Write an ogg OPUS file.


Parameters:

* `$out`: `\Amp\ByteStream\WritableStream`   
* `$streamId`: `?int`   


#### See also: 
* `\Amp\ByteStream\WritableStream`




### `writeHeader(int $channels, int $sampleRate, string $opusVersion): void`




Parameters:

* `$channels`: `int`   
* `$sampleRate`: `int`   
* `$opusVersion`: `string`   



### `writeChunk(string $chunk, int $granuleDiff, bool $eos): void`




Parameters:

* `$chunk`: `string`   
* `$granuleDiff`: `int`   
* `$eos`: `bool`   



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
