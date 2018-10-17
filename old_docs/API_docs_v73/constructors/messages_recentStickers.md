---
title: messages.recentStickers
description: messages_recentStickers attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.recentStickers  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](../types/int.md) | Yes|
|stickers|Array of [Document](../types/Document.md) | Yes|



### Type: [messages\_RecentStickers](../types/messages_RecentStickers.md)


### Example:

```php
$messages_recentStickers = ['_' => 'messages.recentStickers', 'hash' => int, 'stickers' => [Document, Document]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.recentStickers", "hash": int, "stickers": [Document]}
```


Or, if you're into Lua:

```lua
messages_recentStickers={_='messages.recentStickers', hash=int, stickers={Document}}

```


