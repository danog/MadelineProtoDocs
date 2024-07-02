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
* [`testFibers(int $fiberCount = 100000): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`](#testFibers)
* [`getMaps(): ?int`](#getMaps)
* [`getMaxMaps(): ?int`](#getMaxMaps)
* [`stringToStream(string $str): \Amp\ByteStream\ReadableBuffer`](#stringToStream)
* [`genVectorHash(array<(int|string)> $longs): string`](#genVectorHash)
* [`randomInt(integer $modulus = 0): int`](#randomInt)
* [`random(integer $length): string`](#random)
* [`posmod(int $a, int $b): int`](#posmod)
* [`unpackSignedInt(string $value): int`](#unpackSignedInt)
* [`unpackSignedLong(string $value): int`](#unpackSignedLong)
* [`unpackSignedLongString((string|int|array) $value): string`](#unpackSignedLongString)
* [`packSignedInt(integer $value): string`](#packSignedInt)
* [`packSignedLong(int $value): string`](#packSignedLong)
* [`packUnsignedInt(int $value): string`](#packUnsignedInt)
* [`packDouble(float $value): string`](#packDouble)
* [`unpackDouble(string $value): float`](#unpackDouble)
* [`isArrayOrAlike(mixed $var): bool`](#isArrayOrAlike)
* [`arr(mixed ...$params): array`](#arr)
* [`base64urlDecode(string $data): string`](#base64urlDecode)
* [`base64urlEncode(string $data): string`](#base64urlEncode)
* [`rleDecode(string $string): string`](#rleDecode)
* [`rleEncode(string $string): string`](#rleEncode)
* [`inflateStripped(string $stripped): string`](#inflateStripped)
* [`closeConnection(string $message): void`](#closeConnection)
* [`end(array<T> $what): T`](#end)
* [`isAltervista(): bool`](#isAltervista)
* [`openFileAppendOnly(string $path): \Amp\File\File`](#openFileAppendOnly)
* [`getStreamPipe(): \Amp\ByteStream\Pipe`](#getStreamPipe)
* [`openBuffered(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL): Closure(int): ?string`](#openBuffered)
* [`validateEventHandlerClass(class-string<\danog\MadelineProto\EventHandler> $class): list<\danog\MadelineProto\EventHandlerIssue>`](#validateEventHandlerClass)
* [`canConvertOgg(): bool`](#canConvertOgg)
* [`canUseFFmpeg(?\Amp\Cancellation $cancellation = NULL): bool`](#canUseFFmpeg)
* [`rethrow(\Throwable $e): void`](#rethrow)
* [`callFork(\Generator|\Amp\Future|callable $callable, mixed ...$args): \Amp\Future<T>`](#callFork)
* [`flock(string $file, integer $operation, float $polling = 0.1, ?\Amp\Cancellation $token = NULL, ?\Closure $failureCb = NULL): ($token is null ? Closure(): void : (Closure(): void | null))`](#flock)
* [`sleep(float $time): void`](#sleep)
* [`readLine(string $prompt = '', ?\Amp\Cancellation $cancel = NULL): string`](#readLine)
* [`echo(string $string): void`](#echo)
* [`mbStrlen(string $text): int`](#mbStrlen)
* [`mbSubstr(string $text, integer $offset, (null|int) $length = NULL): string`](#mbSubstr)
* [`mbStrSplit(string $text, integer $length): array<string>`](#mbStrSplit)
* [`htmlToMessageEntities(string $html): \danog\MadelineProto\TextEntities`](#htmlToMessageEntities)
* [`markdownToMessageEntities(string $markdown): \danog\MadelineProto\TextEntities`](#markdownToMessageEntities)
* [`entitiesToHtml(string $message, list<(\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity|array{_: string, offset: int, length: int})> $entities, bool $allowTelegramTags = false): string`](#entitiesToHtml)
* [`toCamelCase(string $input): string`](#toCamelCase)
* [`toSnakeCase(string $input): string`](#toSnakeCase)
* [`htmlEscape(string $what): string`](#htmlEscape)
* [`markdownEscape(string $what): string`](#markdownEscape)
* [`markdownCodeblockEscape(string $what): string`](#markdownCodeblockEscape)
* [`markdownCodeEscape(string $what): string`](#markdownCodeEscape)
* [`markdownUrlEscape(string $what): string`](#markdownUrlEscape)
* [`getMimeFromExtension(string $extension, string $default): string`](#getMimeFromExtension)
* [`getExtensionFromMime(string $mime): string`](#getExtensionFromMime)
* [`getExtensionFromLocation(mixed $location, string $default): string`](#getExtensionFromLocation)
* [`getMimeFromFile(string $file): string`](#getMimeFromFile)
* [`getMimeFromBuffer(string $buffer): string`](#getMimeFromBuffer)

## Methods:
### <a name="testFibers"></a> `testFibers(int $fiberCount = 100000): array{maxFibers: int, realMemoryMb: int, maps: ?int, maxMaps: ?int}`

Test fibers.


Parameters:

* `$fiberCount`: `int`   



### <a name="getMaps"></a> `getMaps(): ?int`

Get current number of memory-mapped regions, UNIX only.



### <a name="getMaxMaps"></a> `getMaxMaps(): ?int`

Get maximum number of memory-mapped regions, UNIX only.
Use testFibers to get the maximum number of fibers on any platform.  



### <a name="stringToStream"></a> `stringToStream(string $str): \Amp\ByteStream\ReadableBuffer`

Converts a string into an async amphp stream.


Parameters:

* `$str`: `string`   


#### See also: 
* `\Amp\ByteStream\ReadableBuffer`




### <a name="genVectorHash"></a> `genVectorHash(array<(int|string)> $longs): string`

Generate MTProto vector hash.
  
Returns a vector hash.  


Parameters:

* `$longs`: `array<(int|string)>` IDs  



### <a name="randomInt"></a> `randomInt(integer $modulus = 0): int`

Get random integer.


Parameters:

* `$modulus`: `integer` Modulus  



### <a name="random"></a> `random(integer $length): string`

Get secure random string of specified length.


Parameters:

* `$length`: `integer` Length  



### <a name="posmod"></a> `posmod(int $a, int $b): int`

Positive modulo
Works just like the % (modulus) operator, only returns always a postive number.  


Parameters:

* `$a`: `int` A  
* `$b`: `int` B  



### <a name="unpackSignedInt"></a> `unpackSignedInt(string $value): int`

Unpack base256 signed int.


Parameters:

* `$value`: `string` base256 int  



### <a name="unpackSignedLong"></a> `unpackSignedLong(string $value): int`

Unpack base256 signed long.


Parameters:

* `$value`: `string` base256 long  



### <a name="unpackSignedLongString"></a> `unpackSignedLongString((string|int|array) $value): string`

Unpack base256 signed long to string.


Parameters:

* `$value`: `(string|int|array)` base256 long  



### <a name="packSignedInt"></a> `packSignedInt(integer $value): string`

Convert integer to base256 signed int.


Parameters:

* `$value`: `integer` Value to convert  



### <a name="packSignedLong"></a> `packSignedLong(int $value): string`

Convert integer to base256 long.


Parameters:

* `$value`: `int` Value to convert  



### <a name="packUnsignedInt"></a> `packUnsignedInt(int $value): string`

Convert value to unsigned base256 int.


Parameters:

* `$value`: `int` Value  



### <a name="packDouble"></a> `packDouble(float $value): string`

Convert double to binary version.


Parameters:

* `$value`: `float` Value to convert  



### <a name="unpackDouble"></a> `unpackDouble(string $value): float`

Unpack binary double.


Parameters:

* `$value`: `string` Value to unpack  



### <a name="isArrayOrAlike"></a> `isArrayOrAlike(mixed $var): bool`

Check if is array or similar (traversable && countable && arrayAccess).


Parameters:

* `$var`: `mixed` Value to check  



### <a name="arr"></a> `arr(mixed ...$params): array`

Create array.


Parameters:

* `...$params`: `mixed` Params  



### <a name="base64urlDecode"></a> `base64urlDecode(string $data): string`

base64URL decode.


Parameters:

* `$data`: `string` Data to decode  



### <a name="base64urlEncode"></a> `base64urlEncode(string $data): string`

Base64URL encode.


Parameters:

* `$data`: `string` Data to encode  



### <a name="rleDecode"></a> `rleDecode(string $string): string`

null-byte RLE decode.


Parameters:

* `$string`: `string` Data to decode  



### <a name="rleEncode"></a> `rleEncode(string $string): string`

null-byte RLE encode.


Parameters:

* `$string`: `string` Data to encode  



### <a name="inflateStripped"></a> `inflateStripped(string $stripped): string`

Inflate stripped photosize to full JPG payload.


Parameters:

* `$stripped`: `string` Stripped photosize  



### <a name="closeConnection"></a> `closeConnection(string $message): void`

Close connection with client, connected via web.


Parameters:

* `$message`: `string` Message  



### <a name="end"></a> `end(array<T> $what): T`

Get final element of array.


Parameters:

* `$what`: `array<T>` Array  



### <a name="isAltervista"></a> `isAltervista(): bool`

Whether this is altervista.



### <a name="openFileAppendOnly"></a> `openFileAppendOnly(string $path): \Amp\File\File`

Opens a file in append-only mode.


Parameters:

* `$path`: `string` File path.  


#### See also: 
* `\Amp\File\File`




### <a name="getStreamPipe"></a> `getStreamPipe(): \Amp\ByteStream\Pipe`

Obtains a pipe that can be used to upload a file from a stream.


#### See also: 
* `\Amp\ByteStream\Pipe`




### <a name="openBuffered"></a> `openBuffered(\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream $stream, ?\Amp\Cancellation $cancellation = NULL): Closure(int): ?string`

Provide a buffered reader for a file, URL or amp stream.


Parameters:

* `$stream`: `\danog\MadelineProto\LocalFile|\danog\MadelineProto\RemoteUrl|\Amp\ByteStream\ReadableStream`   
* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* [`\danog\MadelineProto\LocalFile`: Indicates a local file to upload.](../../danog/MadelineProto/LocalFile.html)
* [`\danog\MadelineProto\RemoteUrl`: Indicates a remote URL to upload.](../../danog/MadelineProto/RemoteUrl.html)
* `\Amp\ByteStream\ReadableStream`
* `\Amp\Cancellation`




### <a name="validateEventHandlerClass"></a> `validateEventHandlerClass(class-string<\danog\MadelineProto\EventHandler> $class): list<\danog\MadelineProto\EventHandlerIssue>`

Perform static analysis on a certain event handler class, to make sure it satisfies some performance requirements.


Parameters:

* `$class`: `class-string<\danog\MadelineProto\EventHandler>` Class name  


#### See also: 
* [`\danog\MadelineProto\EventHandler`: Event handler.](../../danog/MadelineProto/EventHandler.html)
* [`\danog\MadelineProto\EventHandlerIssue`: Represents an event handler issue.](../../danog/MadelineProto/EventHandlerIssue.html)




### <a name="canConvertOgg"></a> `canConvertOgg(): bool`

Whether we can convert any audio/video file to a VoIP OGG OPUS file, or the files must be preconverted using @libtgvoipbot.



### <a name="canUseFFmpeg"></a> `canUseFFmpeg(?\Amp\Cancellation $cancellation = NULL): bool`

Whether we can convert any audio/video file using ffmpeg.


Parameters:

* `$cancellation`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### <a name="rethrow"></a> `rethrow(\Throwable $e): void`

Rethrow exception into event loop.


Parameters:

* `$e`: `\Throwable`   


#### See also: 
* `\Throwable`




### <a name="callFork"></a> `callFork(\Generator|\Amp\Future|callable $callable, mixed ...$args): \Amp\Future<T>`

Fork a new green thread and execute the passed function in the background.


Parameters:

* `$callable`: `\Generator|\Amp\Future|callable`   
* `...$args`: `mixed` Arguments forwarded to the function when forking the thread.  


#### See also: 
* `\Generator`
* `\Amp\Future`




### <a name="flock"></a> `flock(string $file, integer $operation, float $polling = 0.1, ?\Amp\Cancellation $token = NULL, ?\Closure $failureCb = NULL): ($token is null ? Closure(): void : (Closure(): void | null))`

Asynchronously lock a file
Resolves with a callbable that MUST eventually be called in order to release the lock.  


Parameters:

* `$file`: `string` File to lock  
* `$operation`: `integer` Locking mode  
* `$polling`: `float` Polling interval  
* `$token`: `?\Amp\Cancellation` Cancellation token  
* `$failureCb`: `?\Closure` Failure callback, called only once if the first locking attempt fails.  


#### See also: 
* `\Amp\Cancellation`
* `\Closure`




### <a name="sleep"></a> `sleep(float $time): void`

Asynchronously sleep.


Parameters:

* `$time`: `float` Number of seconds to sleep for  



### <a name="readLine"></a> `readLine(string $prompt = '', ?\Amp\Cancellation $cancel = NULL): string`

Asynchronously read line.


Parameters:

* `$prompt`: `string` Prompt  
* `$cancel`: `?\Amp\Cancellation`   


#### See also: 
* `\Amp\Cancellation`




### <a name="echo"></a> `echo(string $string): void`

Asynchronously write to stdout/browser.


Parameters:

* `$string`: `string` Message to echo  



### <a name="mbStrlen"></a> `mbStrlen(string $text): int`

Get Telegram UTF-8 length of string.


Parameters:

* `$text`: `string` Text  



### <a name="mbSubstr"></a> `mbSubstr(string $text, integer $offset, (null|int) $length = NULL): string`

Telegram UTF-8 multibyte substring.


Parameters:

* `$text`: `string` Text to substring  
* `$offset`: `integer` Offset  
* `$length`: `(null|int)` Length  



### <a name="mbStrSplit"></a> `mbStrSplit(string $text, integer $length): array<string>`

Telegram UTF-8 multibyte split.


Parameters:

* `$text`: `string` Text  
* `$length`: `integer` Length  



### <a name="htmlToMessageEntities"></a> `htmlToMessageEntities(string $html): \danog\MadelineProto\TextEntities`

Manually convert HTML to a message and a set of entities.
  
NOTE: You don't have to use this method to send HTML messages.  
  
This method is already called automatically by using parse_mode: "HTML" in messages.sendMessage, messages.sendMedia, et cetera...  


Parameters:

* `$html`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)
* [`\danog\MadelineProto\TextEntities`: Class that converts HTML or markdown to a message + set of entities.](../../danog/MadelineProto/TextEntities.html)




### <a name="markdownToMessageEntities"></a> `markdownToMessageEntities(string $markdown): \danog\MadelineProto\TextEntities`

Manually convert markdown to a message and a set of entities.
  
NOTE: You don't have to use this method to send Markdown messages.  
  
This method is already called automatically by using parse_mode: "Markdown" in messages.sendMessage, messages.sendMedia, et cetera...  


Parameters:

* `$markdown`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)
* [`\danog\MadelineProto\TextEntities`: Class that converts HTML or markdown to a message + set of entities.](../../danog/MadelineProto/TextEntities.html)




### <a name="entitiesToHtml"></a> `entitiesToHtml(string $message, list<(\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity|array{_: string, offset: int, length: int})> $entities, bool $allowTelegramTags = false): string`

Convert a message and a set of entities to HTML.


Parameters:

* `$message`: `string`   
* `$entities`: `list<(\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity|array{_: string, offset: int, length: int})>`   
* `$allowTelegramTags`: `bool` Whether to allow telegram-specific tags like tg-spoiler, tg-emoji, mention links and so on...  


#### See also: 
* [`\danog\MadelineProto\EventHandler\Message\Entities\MessageEntity`: Master class for message entities.](../../danog/MadelineProto/EventHandler/Message/Entities/MessageEntity.html)




### <a name="toCamelCase"></a> `toCamelCase(string $input): string`

Convert to camelCase.


Parameters:

* `$input`: `string` String  



### <a name="toSnakeCase"></a> `toSnakeCase(string $input): string`

Convert to snake_case.


Parameters:

* `$input`: `string` String  



### <a name="htmlEscape"></a> `htmlEscape(string $what): string`

Escape string for MadelineProto's HTML entity converter.


Parameters:

* `$what`: `string` String to escape  



### <a name="markdownEscape"></a> `markdownEscape(string $what): string`

Escape string for markdown.


Parameters:

* `$what`: `string` String to escape  



### <a name="markdownCodeblockEscape"></a> `markdownCodeblockEscape(string $what): string`

Escape string for markdown codeblock.


Parameters:

* `$what`: `string` String to escape  



### <a name="markdownCodeEscape"></a> `markdownCodeEscape(string $what): string`

Escape string for markdown code section.


Parameters:

* `$what`: `string` String to escape  



### <a name="markdownUrlEscape"></a> `markdownUrlEscape(string $what): string`

Escape string for URL.


Parameters:

* `$what`: `string` String to escape  



### <a name="getMimeFromExtension"></a> `getMimeFromExtension(string $extension, string $default): string`

Get mime type from file extension.


Parameters:

* `$extension`: `string` File extension  
* `$default`: `string` Default mime type  



### <a name="getExtensionFromMime"></a> `getExtensionFromMime(string $mime): string`

Get extension from mime type.


Parameters:

* `$mime`: `string` MIME type  



### <a name="getExtensionFromLocation"></a> `getExtensionFromLocation(mixed $location, string $default): string`

Get extension from file location.


Parameters:

* `$location`: `mixed` File location  
* `$default`: `string` Default extension  



### <a name="getMimeFromFile"></a> `getMimeFromFile(string $file): string`

Get mime type of file.


Parameters:

* `$file`: `string` File  



### <a name="getMimeFromBuffer"></a> `getMimeFromBuffer(string $buffer): string`

Get mime type from buffer.


Parameters:

* `$buffer`: `string` Buffer  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
