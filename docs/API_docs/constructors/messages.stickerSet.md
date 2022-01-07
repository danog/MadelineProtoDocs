---
title: "messages.stickerSet"
description: "Stickerset and stickers inside it"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_stickerSet.html
---
# Constructor: messages.stickerSet  
[Back to constructors index](/API_docs/constructors/index.md)



Stickerset and stickers inside it

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|set|[StickerSet](/API_docs/types/StickerSet.md) | Yes|The stickerset|
|packs|Array of [StickerPack](/API_docs/types/StickerPack.md) | Yes|Emoji info for stickers|
|documents|Array of [Document](/API_docs/types/Document.md) | Yes|Stickers in stickerset|



### Type: [messages.StickerSet](/API_docs/types/messages.StickerSet.md)


### Example:

```php
$messages_stickerSet = ['_' => 'messages.stickerSet', 'set' => StickerSet, 'packs' => [StickerPack, StickerPack], 'documents' => [Document, Document]];
```  
