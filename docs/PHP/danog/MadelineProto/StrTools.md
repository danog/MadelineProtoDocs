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
* [`mbStrlen(string $text): int`](#mbStrlen)
* [`mbSubstr(string $text, integer $offset, (null|int) $length = NULL): string`](#mbSubstr)
* [`mbStrSplit(string $text, integer $length): array<string>`](#mbStrSplit)
* [`htmlToMessageEntities(string $html): \danog\MadelineProto\TL\Conversion\DOMEntities`](#htmlToMessageEntities)
* [`markdownToMessageEntities(string $markdown): \danog\MadelineProto\TL\Conversion\MarkdownEntities`](#markdownToMessageEntities)
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



### <a name="htmlToMessageEntities"></a> `htmlToMessageEntities(string $html): \danog\MadelineProto\TL\Conversion\DOMEntities`

Manually convert HTML to a message and a set of entities.
  
NOTE: You don't have to use this method to send HTML messages.  
  
This method is already called automatically by using parse_mode: "HTML" in messages.sendMessage, messages.sendMedia, et cetera...  


Parameters:

* `$html`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)
* [`\danog\MadelineProto\TL\Conversion\DOMEntities`: Class that converts HTML to a message + set of entities.](../../danog/MadelineProto/TL/Conversion/DOMEntities.html)




### <a name="markdownToMessageEntities"></a> `markdownToMessageEntities(string $markdown): \danog\MadelineProto\TL\Conversion\MarkdownEntities`

Manually convert markdown to a message and a set of entities.
  
NOTE: You don't have to use this method to send Markdown messages.  
  
This method is already called automatically by using parse_mode: "Markdown" in messages.sendMessage, messages.sendMedia, et cetera...  


Parameters:

* `$markdown`: `string`   


Return value: Object containing message and entities

#### See also: 
* [https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode](https://docs.madelineproto.xyz/API_docs/methods/messages.sendMessage.html#usage-of-parse_mode)
* [`\danog\MadelineProto\TL\Conversion\MarkdownEntities`: Class that converts Markdown to a message + set of entities.](../../danog/MadelineProto/TL/Conversion/MarkdownEntities.html)




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
