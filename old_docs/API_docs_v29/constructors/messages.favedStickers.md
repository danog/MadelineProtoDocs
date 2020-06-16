---
title: messages.favedStickers
description: Favorited stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_favedStickers.html
---
# Constructor: messages.favedStickers  
[Back to constructors index](index.md)



Favorited stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|
|packs|Array of [StickerPack](../types/StickerPack.md) | Yes|Emojis associated to stickers|
|stickers|Array of [Document](../types/Document.md) | Yes|Favorited stickers|



### Type: [messages.FavedStickers](../types/messages.FavedStickers.md)


### Example:

```php
$messages.favedStickers = ['_' => 'messages.favedStickers', 'hash' => int, 'packs' => [StickerPack, StickerPack], 'stickers' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
messages.favedStickers={_='messages.favedStickers', hash=int, packs={StickerPack}, stickers={Document}}

```


