---
title: messages.allStickers
description: All stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.allStickers  
[Back to constructors index](index.md)



All stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[string](../types/string.md) | Yes|Hash|
|packs|Array of [StickerPack](../types/StickerPack.md) | Yes|Packs|
|documents|Array of [Document](../types/Document.md) | Yes|Documents|



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


