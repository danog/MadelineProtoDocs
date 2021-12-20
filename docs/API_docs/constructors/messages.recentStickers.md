---
title: "messages.recentStickers"
description: "Recently used stickers"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_recentStickers.html
---
# Constructor: messages.recentStickers  
[Back to constructors index](index.md)



Recently used stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](../types/long.md) | Yes|
|packs|Array of [StickerPack](../types/StickerPack.md) | Yes|Emojis associated to stickers|
|stickers|Array of [Document](../types/Document.md) | Yes|Recent stickers|
|dates|Array of [int](../types/int.md) | Yes|When was each sticker last used|



### Type: [messages.RecentStickers](../types/messages.RecentStickers.md)


### Example:

```php
$messages_recentStickers = ['_' => 'messages.recentStickers', 'hash' => long, 'packs' => [StickerPack, StickerPack], 'stickers' => [Document, Document], 'dates' => [int, int]];
```  


Or, if you're into Lua:

```lua
messages_recentStickers={_='messages.recentStickers', hash=long, packs={StickerPack}, stickers={Document}, dates={int}}

```


