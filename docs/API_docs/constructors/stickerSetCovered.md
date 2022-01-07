---
title: "stickerSetCovered"
description: "Stickerset, with a specific sticker as preview"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetCovered  
[Back to constructors index](/API_docs/constructors/index.md)



Stickerset, with a specific sticker as preview

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|set|[StickerSet](/API_docs/types/StickerSet.md) | Yes|Stickerset|
|cover|[Document](/API_docs/types/Document.md) | Optional|Preview|



### Type: [StickerSetCovered](/API_docs/types/StickerSetCovered.md)


### Example:

```php
$stickerSetCovered = ['_' => 'stickerSetCovered', 'set' => StickerSet, 'cover' => Document];
```  
