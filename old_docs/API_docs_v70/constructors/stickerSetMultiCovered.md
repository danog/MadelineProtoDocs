---
title: stickerSetMultiCovered
description: Stickerset, with a specific stickers as preview
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetMultiCovered  
[Back to constructors index](index.md)



Stickerset, with a specific stickers as preview

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|set|[StickerSet](../types/StickerSet.md) | Yes|Stickerset|
|covers|Array of [Document](../types/Document.md) | Yes|Covers|



### Type: [StickerSetCovered](../types/StickerSetCovered.md)


### Example:

```php
$stickerSetMultiCovered = ['_' => 'stickerSetMultiCovered', 'set' => StickerSet, 'covers' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
stickerSetMultiCovered={_='stickerSetMultiCovered', set=StickerSet, covers={Document}}

```


