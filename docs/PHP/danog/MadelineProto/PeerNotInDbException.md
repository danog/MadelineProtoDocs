---
title: "danog\\MadelineProto\\PeerNotInDbException: Indicates that a specified peer (user, chat, channel) was not found in the internal MadelineProto peer database."
description: "\nThis can usually be fixed by enabling `setFullFetch(true)` in the [peer database settings](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Settings/Peer.html#setfullfetch-bool-fullfetch-self).\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\PeerNotInDbException`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Indicates that a specified peer (user, chat, channel) was not found in the internal MadelineProto peer database.  


This can usually be fixed by enabling `setFullFetch(true)` in the [peer database settings](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Settings/Peer.html#setfullfetch-bool-fullfetch-self).


## Properties
* `$tlTrace`: `string` TL trace.

## Method list:
* [`__construct()`](#__construct)
* [`extension(string $extensionName): self`](#extension)
* [`getMessage(): string`](#getMessage)
* [`getCode()`](#getCode)
* [`getFile(): string`](#getFile)
* [`getLine(): int`](#getLine)
* [`getTrace(): array`](#getTrace)
* [`getPrevious(): ?Throwable`](#getPrevious)
* [`getTraceAsString(): string`](#getTraceAsString)
* [`getTLTrace(): string`](#getTLTrace)

## Methods:
### <a name="__construct"></a> `__construct()`





### <a name="extension"></a> `extension(string $extensionName): self`

Complain about missing extensions.


Parameters:

* `$extensionName`: `string` Extension name  



### <a name="getMessage"></a> `getMessage(): string`





### <a name="getCode"></a> `getCode()`





### <a name="getFile"></a> `getFile(): string`





### <a name="getLine"></a> `getLine(): int`





### <a name="getTrace"></a> `getTrace(): array`





### <a name="getPrevious"></a> `getPrevious(): ?Throwable`




#### See also: 
* `Throwable`




### <a name="getTraceAsString"></a> `getTraceAsString(): string`





### <a name="getTLTrace"></a> `getTLTrace(): string`

Get TL trace.



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
