---
title: messages.allStickers
description: messages_allStickers attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.allStickers  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[string](../types/string.md) | Yes|
|packs|Array of [StickerPack](../types/StickerPack.md) | Yes|
|documents|Array of [Document](../types/Document.md) | Yes|



### Type: [messages\_AllStickers](../types/messages_AllStickers.md)


### Example:

```php
$messages_allStickers = ['_' => 'messages.allStickers', 'hash' => 'string', 'packs' => [StickerPack, StickerPack], 'documents' => [Document, Document]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.allStickers", "hash": "string", "packs": [StickerPack], "documents": [Document]}
```


Or, if you're into Lua:

```lua
messages_allStickers={_='messages.allStickers', hash='string', packs={StickerPack}, documents={Document}}

```


