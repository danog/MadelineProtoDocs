---
title: "stickerSetCovered"
description: "Stickerset, with a specific sticker as preview"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetCovered  
[Back to constructors index](/API_docs/constructors/index.html)



Stickerset, with a specific sticker as preview

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|set|[StickerSet](/API_docs/types/StickerSet.html) | Yes|Stickerset|
|cover|[Document](/API_docs/types/Document.html) | Optional|Preview|



### Type: [StickerSetCovered](/API_docs/types/StickerSetCovered.html)


### Example:

```
$stickerSetCovered = ['_' => 'stickerSetCovered', 'set' => StickerSet, 'cover' => Document];
```  
