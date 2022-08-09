---
title: "stickerSetFullCovered"
description: "stickerSetFullCovered attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetFullCovered  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|set|[StickerSet](/API_docs/types/StickerSet.html) | Yes|
|packs|Array of [StickerPack](/API_docs/types/StickerPack.html) | Yes|
|documents|Array of [Document](/API_docs/types/Document.html) | Yes|



### Type: [StickerSetCovered](/API_docs/types/StickerSetCovered.html)


### Example:

```
$stickerSetFullCovered = ['_' => 'stickerSetFullCovered', 'set' => StickerSet, 'packs' => [StickerPack, StickerPack], 'documents' => [Document, Document]];
```  
