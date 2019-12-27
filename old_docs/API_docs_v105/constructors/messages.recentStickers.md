---
title: messages.recentStickers
description: Recently used stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_recentStickers.html
---
# Constructor: messages.recentStickers  
[Back to constructors index](index.md)



Recently used stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|packs|Array of [StickerPack](../types/StickerPack.md) | Yes|Packs|
|stickers|Array of [Document](../types/Document.md) | Yes|Stickers|
|dates|Array of [int](../types/int.md) | Yes|Dates|



### Type: [messages.RecentStickers](../types/messages.RecentStickers.md)


### Example:

```php
$messages.recentStickers = ['_' => 'messages.recentStickers', 'hash' => int, 'packs' => [StickerPack, StickerPack], 'stickers' => [Document, Document], 'dates' => [int, int]];
```  


Or, if you're into Lua:

```lua
messages.recentStickers={_='messages.recentStickers', hash=int, packs={StickerPack}, stickers={Document}, dates={int}}

```


