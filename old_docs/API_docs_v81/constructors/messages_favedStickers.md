---
title: messages.favedStickers
description: Faved stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.favedStickers  
[Back to constructors index](index.md)



Faved stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|Hash|
|packs|Array of [StickerPack](../types/StickerPack.md) | Yes|Packs|
|stickers|Array of [Document](../types/Document.md) | Yes|Stickers|



### Type: [messages\_FavedStickers](../types/messages_FavedStickers.md)


### Example:

```php
$messages_favedStickers = ['_' => 'messages.favedStickers', 'hash' => int, 'packs' => [StickerPack, StickerPack], 'stickers' => [Document, Document]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.favedStickers", "hash": int, "packs": [StickerPack], "stickers": [Document]}
```


Or, if you're into Lua:

```lua
messages_favedStickers={_='messages.favedStickers', hash=int, packs={StickerPack}, stickers={Document}}

```


