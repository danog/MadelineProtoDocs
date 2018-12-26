---
title: stickerSetMultiCovered
description: Sticker set multi covered
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetMultiCovered  
[Back to constructors index](index.md)



Sticker set multi covered

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|set|[StickerSet](../types/StickerSet.md) | Yes|Set|
|covers|Array of [Document](../types/Document.md) | Yes|Covers|



### Type: [StickerSetCovered](../types/StickerSetCovered.md)


### Example:

```php
$stickerSetMultiCovered = ['_' => 'stickerSetMultiCovered', 'set' => StickerSet, 'covers' => [Document, Document]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "stickerSetMultiCovered", "set": StickerSet, "covers": [Document]}
```


Or, if you're into Lua:

```lua
stickerSetMultiCovered={_='stickerSetMultiCovered', set=StickerSet, covers={Document}}

```


