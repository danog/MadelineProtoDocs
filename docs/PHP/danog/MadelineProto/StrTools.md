---
title: "danog\\MadelineProto\\StrTools: Some tools."
description: ""
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\StrTools`
[Back to index](../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

Some tools.  




## Constants
* `danog\MadelineProto\StrTools::ALL_MIMES`: 


## Method list:
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
