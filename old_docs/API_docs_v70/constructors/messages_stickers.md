---
title: messages.stickers
description: Stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.stickers  
[Back to constructors index](index.md)



Stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[string](../types/string.md) | Yes|Hash|
|stickers|Array of [Document](../types/Document.md) | Yes|Stickers|



### Type: [messages\_Stickers](../types/messages_Stickers.md)


### Example:

```php
$messages_stickers = ['_' => 'messages.stickers', 'hash' => 'string', 'stickers' => [Document, Document]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.stickers", "hash": "string", "stickers": [Document]}
```


Or, if you're into Lua:

```lua
messages_stickers={_='messages.stickers', hash='string', stickers={Document}}

```


