---
title: "danog\\MadelineProto\\Tools: Some tools."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Tools`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Some tools.  




## Constants
* `danog\MadelineProto\Tools::ALL_MIMES`: 


## Method list:
* [`testFibers(int $fiberCount = 100000): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`](#testfibers)
* [`getMaps(): ?int`](#getmaps)
* [`getMaxMaps(): ?int`](#getmaxmaps)
* [`stringToStream(string $str): \Amp\ByteStream\ReadableBuffer`](#stringtostream)
* [`genVectorHash(array $longs): string`](#genvectorhash)
* [`randomInt(int $modulus = 0): int`](#randomint)
* [`random(int $length): string`](#random)
* [`posmod(int $a, int $b): int`](#posmod)
* [`unpackSignedInt(string $value): int`](#unpacksignedint)
* [`unpackSignedLong(string $value): int`](#unpacksignedlong)
* [`unpackSignedLongString(string|int|array $value): string`](#unpacksignedlongstring)
* [`packSignedInt(int $value): string`](#packsignedint)
* [`packSignedLong(int $value): string`](#packsignedlong)
* [`packUnsignedInt(int $value): string`](#packunsignedint)
* [`packDouble(float $value): string`](#packdouble)
* [`unpackDouble(string $value): float`](#unpackdouble)
* [`isArrayOrAlike(mixed $var): bool`](#isarrayoralike)
* [`arr(mixed ...$params): array`](#arr)
* [`base64urlDecode(string $data): string`](#base64urldecode)
* [`base64urlEncode(string $data): string`](#base64urlencode)
* [`rleDecode(string $string): string`](#rledecode)
* [`rleEncode(string $string): string`](#rleencode)
* [`inflateStripped(string $stripped): string`](#inflatestripped)
* [`closeConnection(string $message): void`](#closeconnection)
* [`end(\T[] $what): \T`](#end)
* [`isAltervista(): bool`](#isaltervista)
* [`openFileAppendOnly(string $path): \Amp\File\File`](#openfileappendonly)
* [`getStreamPipe(): \Amp\ByteStream\Pipe`](#getstreampipe)
* [`openBuffered(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL): callable`](#openbuffered)
* [`validateEventHandlerClass(class-string<\danog\MadelineProto\EventHandler> $class): list<\danog\MadelineProto\EventHandlerIssue>`](#validateeventhandlerclass)
* [`canConvertOgg(): bool`](#canconvertogg)
* [`rethrow(\Throwable $e): void`](#rethrow)
* [`callFork(\Generator|\Amp\Future|callable $callable, mixed ...$args): \Amp\Future<\T>`](#callfork)
* [`flock(string $file, int $operation, float $polling = 0.1, ?\Amp\Cancellation $token = NULL, ?\Closure $failureCb = NULL): mixed`](#flock)
* [`sleep(float $time): void`](#sleep)
* [`readLine(string $prompt = '', ?\Amp\Cancellation $cancel = NULL): string`](#readline)
* [`echo(string $string): void`](#echo)
* [`mbStrlen(string $text): int`](#mbstrlen)
* [`mbSubstr(string $text, int $offset, null|int $length = NULL): string`](#mbsubstr)
* [`mbStrSplit(string $text, int $length): string[]`](#mbstrsplit)
* [`htmlToMessageEntities(string $html): \danog\MadelineProto\TL\Conversion\DOMEntities Object containing message and entities`](#htmltomessageentities)
* [`markdownToMessageEntities(string $markdown): \danog\MadelineProto\TL\Conversion\MarkdownEntities Object containing message and entities`](#markdowntomessageentities)
* [`entitiesToHtml(string $message, list<\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity|array{_: string, offset: int, length: int}> $entities, bool $allowTelegramTags = false): string`](#entitiestohtml)
* [`toCamelCase(string $input): string`](#tocamelcase)
* [`toSnakeCase(string $input): string`](#tosnakecase)
* [`markdownEscape(string $what): string`](#markdownescape)
* [`markdownCodeblockEscape(string $what): string`](#markdowncodeblockescape)
* [`markdownUrlEscape(string $what): string`](#markdownurlescape)
* [`getMimeFromExtension(string $extension, string $default): string`](#getmimefromextension)
* [`getExtensionFromMime(string $mime): string`](#getextensionfrommime)
* [`getExtensionFromLocation(mixed $location, string $default): string`](#getextensionfromlocation)
* [`getMimeFromFile(string $file): string`](#getmimefromfile)
* [`getMimeFromBuffer(string $buffer): string`](#getmimefrombuffer)

## Methods:
### `testFibers(int $fiberCount = 100000): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`

Test fibers.


Parameters:

* `$fiberCount`: `int`   



### `getMaps(): ?int`

Get current number of memory-mapped regions, UNIX only.



### `getMaxMaps(): ?int`

Get maximum number of memory-mapped regions, UNIX only.
Use testFibers to get the maximum number of fibers on any platform.


### `stringToStream(string $str): \Amp\ByteStream\ReadableBuffer`

Converts a string into an async amphp stream.


Parameters:

* `$str`: `string`   


#### See also: 
* `\Amp\ByteStream\ReadableBuffer`




### `genVectorHash(array $longs): string`

Generate MTProto vector hash.
Returns a vector hash.

Parameters:

* `$longs`: `array` IDs  



### `randomInt(int $modulus = 0): int`

Get random integer.


Parameters:

* `$modulus`: `int` Modulus  



### `random(int $length): string`

Get secure random string of specified length.


Parameters:

* `$length`: `int` Length  



### `posmod(int $a, int $b): int`

Positive modulo
Works just like the % (modulus) operator, only returns always a postive number.


Parameters:

* `$a`: `int` A  
* `$b`: `int` B  



### `unpackSignedInt(string $value): int`

Unpack base256 signed int.


Parameters:

* `$value`: `string` base256 int  



### `unpackSignedLong(string $value): int`

Unpack base256 signed long.


Parameters:

* `$value`: `string` base256 long  



### `unpackSignedLongString(string|int|array $value): string`

Unpack base256 signed long to string.


Parameters:

* `$value`: `string|int|array` base256 long  



### `packSignedInt(int $value): string`

Convert integer to base256 signed int.


Parameters:

* `$value`: `int` Value to convert  



### `packSignedLong(int $value): string`

Convert integer to base256 long.


Parameters:

* `$value`: `int` Value to convert  



### `packUnsignedInt(int $value): string`

Convert value to unsigned base256 int.


Parameters:

* `$value`: `int` Value  



### `packDouble(float $value): string`

Convert double to binary version.


Parameters:

* `$value`: `float` Value to convert  



### `unpackDouble(string $value): float`

Unpack binary double.


Parameters:

* `$value`: `string` Value to unpack  



### `isArrayOrAlike(mixed $var): bool`

Check if is array or similar (traversable && countable && arrayAccess).


Parameters:

* `$var`: `mixed` Value to check  



### `arr(mixed ...$params): array`

Create array.


Parameters:

* `...$params`: `mixed` Params  



### `base64urlDecode(string $data): string`

base64URL decode.


Parameters:

* `$data`: `string` Data to decode  



### `base64urlEncode(string $data): string`

Base64URL encode.


Parameters:

* `$data`: `string` Data to encode  



### `rleDecode(string $string): string`

null-byte RLE decode.


Parameters:

* `$string`: `string` Data to decode  



### `rleEncode(string $string): string`

null-byte RLE encode.


Parameters:

* `$string`: `string` Data to encode  



### `inflateStripped(string $stripped): string`

Inflate stripped photosize to full JPG payload.


Parameters:

* `$stripped`: `string` Stripped photosize  



### `closeConnection(string $message): void`

Close connection with client, connected via web.


Parameters:

* `$message`: `string` Message  



### `end(\T[] $what): \T`

Get final element of array.


Parameters:

* `$what`: `\T[]` Array  


#### See also: 
* `\T`




### `isAltervista(): bool`

Whether this is altervista.



### `openFileAppendOnly(string $path): \Amp\File\File`

Opens a file in append-only mode.


Parameters:

* `$path`: `string` File path.  


#### See also: 
* `\Amp\File\File`




### `getStreamPipe(): \Amp\ByteStream\Pipe`

Obtains a pipe that can be used to upload a file from a stream.


#### See also: 
* `\Amp\ByteStream\Pipe`




### `openBuffered(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL): callable`

Provide a buffered reader for a file, URL or amp stream.


Parameters:

* `$stream`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\Cancellation`




### `validateEventHandlerClass(class-string<\danog\MadelineProto\EventHandler> $class): list<\danog\MadelineProto\EventHandlerIssue>`

Perform static analysis on a certain event handler class, to make sure it satisfies some performance requirements.


Parameters:

* `$class`: `class-string<\danog\MadelineProto\EventHandler>` Class name  


#### See also: 
* [`\danog\MadelineProto\EventHandler`: Event handler.](../../danog/MadelineProto/EventHandler.html)
* [`\danog\MadelineProto\EventHandlerIssue`: Represents an event handler issue.](../../danog/MadelineProto/EventHandlerIssue.html)




### `canConvertOgg(): bool`

Whether we can convert any audio/video file to a VoIP OGG OPUS file, or the files must be preconverted using @libtgvoipbot.



### `rethrow(\Throwable $e): void`

Rethrow exception into event loop.


Parameters:

* `$e`: `\Throwable`   


#### See also: 
* `\Throwable`




### `callFork(\Generator|\Amp\Future|callable $callable, mixed ...$args): \Amp\Future<\T>`

Fork a new green thread and execute the passed function in the background.


Parameters:

* `$callable`: `\Generator|\Amp\Future|callable`   
* `...$args`: `mixed` Arguments forwarded to the function when forking the thread.  


#### See also: 
* `\Generator`
* `\Amp\Future`
* `\T`




### `flock(string $file, int $operation, float $polling = 0.1, ?\Amp\Cancellation $token = NULL, ?\Closure $failureCb = NULL): mixed`

Asynchronously lock a file
Resolves with a callbable that MUST eventually be called in order to release the lock.


Parameters:

* `$file`: `string` File to lock  
* `$operation`: `int` Locking mode  
* `$polling`: `float` Polling interval  
* `$token`: `?\Amp\Cancellation` Cancellation token  
* `$failureCb`: `?\Closure` Failure callback, called only once if the first locking attempt fails.  


#### See also: 
* `\Amp\Cancellation`
* `\Closure`




### `sleep(float $time): void`

Asynchronously sleep.


Parameters:

* `$time`: `float` Number of seconds to sleep for  



### `readLine(string $prompt = '', ?\Amp\Cancellation $cancel = NULL): string`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  
* `$cancel`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### `echo(string $string): void`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  



### `mbStrlen(string $text): int`

Get Telegram UTF-8 length of string.


Parameters:

* `$text`: `string` Text  



### `mbSubstr(string $text, int $offset, null|int $length = NULL): string`

Telegram UTF-8 multibyte substring.


Parameters:

* `$text`: `string` Text to substring  
* `$offset`: `int` Offset  
* `$length`: `null|int` Length  



### `mbStrSplit(string $text, int $length): string[]`

Telegram UTF-8 multibyte split.


Parameters:

* `$text`: `string` Text  
* `$length`: `int` Length  



### `htmlToMessageEntities(string $html): \danog\MadelineProto\TL\Conversion\DOMEntities Object containing message and entities`

Manually convert HTML to a message and a set of entities.
NOTE: You don't have to use this method to send HTML messages.  
  
This method is already called automatically by using parse_mode: "HTML" in messages.sendMessage, messages.sendMedia, et cetera...

Parameters:

* `$html`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)




### `markdownToMessageEntities(string $markdown): \danog\MadelineProto\TL\Conversion\MarkdownEntities Object containing message and entities`

Manually convert markdown to a message and a set of entities.
NOTE: You don't have to use this method to send Markdown messages.  
  
This method is already called automatically by using parse_mode: "Markdown" in messages.sendMessage, messages.sendMedia, et cetera...

Parameters:

* `$markdown`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)




### `entitiesToHtml(string $message, list<\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity|array{_: string, offset: int, length: int}> $entities, bool $allowTelegramTags = false): string`

Convert a message and a set of entities to HTML.


Parameters:

* `$message`: `string`   
* `$entities`: `list<\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity|array{_: string, offset: int, length: int}>`   
* `$allowTelegramTags`: `bool` Whether to allow telegram-specific tags like tg-spoiler, tg-emoji, mention links and so on...  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity`: Master class for message entities.](../../danog/MadelineProto/EventHandler/Message/Entities/MessageEntity.html)




### `toCamelCase(string $input): string`

Convert to camelCase.


Parameters:

* `$input`: `string` String  



### `toSnakeCase(string $input): string`

Convert to snake_case.


Parameters:

* `$input`: `string` String  



### `markdownEscape(string $what): string`

Escape string for markdown.


Parameters:

* `$what`: `string` String to escape  



### `markdownCodeblockEscape(string $what): string`

Escape string for markdown codeblock.


Parameters:

* `$what`: `string` String to escape  



### `markdownUrlEscape(string $what): string`

Escape string for URL.


Parameters:

* `$what`: `string` String to escape  



### `getMimeFromExtension(string $extension, string $default): string`

Get mime type from file extension.


Parameters:

* `$extension`: `string` File extension  
* `$default`: `string` Default mime type  



### `getExtensionFromMime(string $mime): string`

Get extension from mime type.


Parameters:

* `$mime`: `string` MIME type  



### `getExtensionFromLocation(mixed $location, string $default): string`

Get extension from file location.


Parameters:

* `$location`: `mixed` File location  
* `$default`: `string` Default extension  



### `getMimeFromFile(string $file): string`

Get mime type of file.


Parameters:

* `$file`: `string` File  



### `getMimeFromBuffer(string $buffer): string`

Get mime type from buffer.


Parameters:

* `$buffer`: `string` Buffer  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
