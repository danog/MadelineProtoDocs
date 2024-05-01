---
title: "danog\\MadelineProto\\AsyncTools: Async tools."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\AsyncTools`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Async tools.  




## Constants
* `danog\MadelineProto\AsyncTools::ALL_MIMES`: 


## Method list:
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
