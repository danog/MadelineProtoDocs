---
title: "stickerSetMultiCovered"
description: "Stickerset, with a specific stickers as preview"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetMultiCovered  
[Back to constructors index](/API_docs/constructors/index.md)



Stickerset, with a specific stickers as preview

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|set|[StickerSet](/API_docs/types/StickerSet.md) | Yes|Stickerset|
|covers|Array of [Document](/API_docs/types/Document.md) | Yes|Preview stickers|



### Type: [StickerSetCovered](/API_docs/types/StickerSetCovered.md)


### Example:

```php
$stickerSetMultiCovered = ['_' => 'stickerSetMultiCovered', 'set' => StickerSet, 'covers' => [Document, Document]];
```  
