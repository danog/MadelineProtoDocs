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
