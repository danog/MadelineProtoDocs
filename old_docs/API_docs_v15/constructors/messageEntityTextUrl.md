---
title: messageEntityTextUrl
description: Message entity representing a [text url](https://google.com): for in-text urls like <https://google.com> use [messageEntityUrl](../constructors/messageEntityUrl.md).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityTextUrl  
[Back to constructors index](index.md)



Message entity representing a [text url](https://google.com): for in-text urls like <https://google.com> use [messageEntityUrl](../constructors/messageEntityUrl.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|
|url|[string](../types/string.md) | Yes|The actual URL|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityTextUrl = ['_' => 'messageEntityTextUrl', 'offset' => int, 'length' => int, 'url' => 'string'];
```  


Or, if you're into Lua:

```lua
messageEntityTextUrl={_='messageEntityTextUrl', offset=int, length=int, url='string'}

```


