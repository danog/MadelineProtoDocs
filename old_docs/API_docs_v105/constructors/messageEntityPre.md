---
title: messageEntityPre
description: Message entity representing a preformatted `codeblock`, allowing the user to specify a programming language for the codeblock.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityPre  
[Back to constructors index](index.md)



Message entity representing a preformatted `codeblock`, allowing the user to specify a programming language for the codeblock.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|
|language|[string](../types/string.md) | Yes|Programming language of the code|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityPre = ['_' => 'messageEntityPre', 'offset' => int, 'length' => int, 'language' => 'string'];
```  


Or, if you're into Lua:

```lua
messageEntityPre={_='messageEntityPre', offset=int, length=int, language='string'}

```


