---
title: "stickerSetFullCovered"
description: "Stickerset preview with all stickers of the stickerset included.  "
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetFullCovered  
[Back to constructors index](/API_docs/constructors/index.html)



Stickerset preview with all stickers of the stickerset included.  
Currently used only for [custom emoji stickersets](https://core.telegram.org/api/custom-emoji), to avoid a further call to [messages.getStickerSet](../methods/messages.getStickerSet.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|set|[StickerSet](/API_docs/types/StickerSet.html) | Yes|Stickerset|
|packs|Array of [StickerPack](/API_docs/types/StickerPack.html) | Yes|Emoji information about every sticker in the stickerset|
|documents|Array of [Document](/API_docs/types/Document.html) | Yes|Stickers|



### Type: [StickerSetCovered](/API_docs/types/StickerSetCovered.html)


### Example:

```
$stickerSetFullCovered = ['_' => 'stickerSetFullCovered', 'set' => StickerSet, 'packs' => [StickerPack, StickerPack], 'documents' => [Document, Document]];
```  
