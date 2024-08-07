---
title: "danog\\MadelineProto\\RPCError\\ReplyMessagesTooMuchError: Each shortcut can contain a maximum of [appConfig.`quick_reply_messages_limit`](https://core.telegram.org/api/config#quick-reply-messages-limit) messages, the limit was reached."
description: "\nNote: this exception is part of the raw API, and thus is not covered by the backwards-compatibility promise.\n\nAlways check the changelog when upgrading, and use tools like Psalm to easily upgrade your code.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\RPCError\ReplyMessagesTooMuchError`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Each shortcut can contain a maximum of [appConfig.`quick_reply_messages_limit`](https://core.telegram.org/api/config#quick-reply-messages-limit) messages, the limit was reached.  


Note: this exception is part of the raw API, and thus is not covered by the backwards-compatibility promise.

Always check the changelog when upgrading, and use tools like Psalm to easily upgrade your code.


## Properties
* `$rpc`: `string` RPC error.
* `$description`: `string` Human-readable description of RPC error.
* `$tlTrace`: `string` TL trace.

## Method list:
* [`getLocalization(): string`](#getLocalization)
* [`getMessage(): string`](#getMessage)
* [`getCode()`](#getCode)
* [`getFile(): string`](#getFile)
* [`getLine(): int`](#getLine)
* [`getTrace(): array`](#getTrace)
* [`getPrevious(): ?Throwable`](#getPrevious)
* [`getTraceAsString(): string`](#getTraceAsString)
* [`getTLTrace(): string`](#getTLTrace)

## Methods:
### <a name="getLocalization"></a> `getLocalization(): string`

Get localized error name.



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
