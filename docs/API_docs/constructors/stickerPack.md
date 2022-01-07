---
title: "stickerPack"
description: "A stickerpack is a group of stickers associated to the same emoji.  "
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerPack  
[Back to constructors index](index.md)



A stickerpack is a group of stickers associated to the same emoji.  
It is **not** a sticker pack the way it is usually intended, you may be looking for a [StickerSet](../types/StickerSet.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](../types/string.md) | Yes|Emoji|
|documents|Array of [long](../types/long.md) | Yes|Stickers|



### Type: [StickerPack](../types/StickerPack.md)


### Example:

```php
$stickerPack = ['_' => 'stickerPack', 'emoticon' => 'string', 'documents' => [long, long]];
```  
