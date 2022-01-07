---
title: "messages.recentStickers"
description: "Recently used stickers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_recentStickers.html
---
# Constructor: messages.recentStickers  
[Back to constructors index](/API_docs/constructors/index.md)



Recently used stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.md) | Yes|
|packs|Array of [StickerPack](/API_docs/types/StickerPack.md) | Yes|Emojis associated to stickers|
|stickers|Array of [Document](/API_docs/types/Document.md) | Yes|Recent stickers|
|dates|Array of [int](/API_docs/types/int.md) | Yes|When was each sticker last used|



### Type: [messages.RecentStickers](/API_docs/types/messages.RecentStickers.md)


### Example:

```php
$messages_recentStickers = ['_' => 'messages.recentStickers', 'hash' => long, 'packs' => [StickerPack, StickerPack], 'stickers' => [Document, Document], 'dates' => [int, int]];
```  
