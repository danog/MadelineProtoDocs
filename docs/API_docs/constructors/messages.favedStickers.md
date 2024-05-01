---
title: "messages.favedStickers"
description: "Favorited stickers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_favedStickers.html
---
# Constructor: messages.favedStickers  
[Back to constructors index](/API_docs/constructors/index.html)



Favorited stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|packs|Array of [StickerPack](/API_docs/types/StickerPack.html) | Yes|Emojis associated to stickers|
|stickers|Array of [Document](/API_docs/types/Document.html) | Yes|Favorited stickers|



### Type: [messages.FavedStickers](/API_docs/types/messages.FavedStickers.html)


### Example:

```
$messages_favedStickers = ['_' => 'messages.favedStickers', 'hash' => long, 'packs' => [StickerPack, StickerPack], 'stickers' => [Document, Document]];
```  
