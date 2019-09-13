---
title: messages.recentStickers
description: Recent stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.recentStickers  
[Back to constructors index](index.md)



Recent stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|Hash|
|packs|Array of [StickerPack](../types/StickerPack.md) | Yes|Packs|
|stickers|Array of [Document](../types/Document.md) | Yes|Stickers|
|dates|Array of [int](../types/int.md) | Yes|Dates|



### Type: [messages\_RecentStickers](../types/messages_RecentStickers.md)


### Example:

```php
$messages_recentStickers = ['_' => 'messages.recentStickers', 'hash' => int, 'packs' => [StickerPack, StickerPack], 'stickers' => [Document, Document], 'dates' => [int, int]];
```  


Or, if you're into Lua:

```lua
messages_recentStickers={_='messages.recentStickers', hash=int, packs={StickerPack}, stickers={Document}, dates={int}}

```


