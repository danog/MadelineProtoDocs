---
title: "stickerPack"
description: "A stickerpack is a group of stickers associated to the same emoji.  "
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerPack  
[Back to constructors index](/API_docs/constructors/index.html)



A stickerpack is a group of stickers associated to the same emoji.  
It is **not** a sticker pack the way it is usually intended, you may be looking for a [StickerSet](../types/StickerSet.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|emoticon|[string](/API_docs/types/string.html) | Yes|Emoji|
|documents|Array of [long](/API_docs/types/long.html) | Yes|Stickers|



### Type: [StickerPack](/API_docs/types/StickerPack.html)


### Example:

```
$stickerPack = ['_' => 'stickerPack', 'emoticon' => 'string', 'documents' => [long, long]];
```  
