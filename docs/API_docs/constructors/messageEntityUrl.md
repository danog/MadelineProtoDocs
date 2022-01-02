---
title: "messageEntityUrl"
description: "Message entity representing an in-text url: https://google.com; for text urls, use messageEntityTextUrl."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityUrl  
[Back to constructors index](index.md)



Message entity representing an in-text url: <https://google.com>; for [text urls](https://google.com), use [messageEntityTextUrl](../constructors/messageEntityTextUrl.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](../types/int.md) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](../types/int.md) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](../types/MessageEntity.md)


### Example:

```php
$messageEntityUrl = ['_' => 'messageEntityUrl', 'offset' => int, 'length' => int];
```  


Or, if you're into Lua:

```lua
messageEntityUrl={_='messageEntityUrl', offset=int, length=int}

```


