---
title: stickerSetCovered
description: Sticker set covered
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetCovered  
[Back to constructors index](index.md)



Sticker set covered

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|set|[StickerSet](../types/StickerSet.md) | Yes|Set|
|cover|[Document](../types/Document.md) | Optional|Cover|



### Type: [StickerSetCovered](../types/StickerSetCovered.md)


### Example:

```php
$stickerSetCovered = ['_' => 'stickerSetCovered', 'set' => StickerSet, 'cover' => Document];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "stickerSetCovered", "set": StickerSet, "cover": Document}
```


Or, if you're into Lua:

```lua
stickerSetCovered={_='stickerSetCovered', set=StickerSet, cover=Document}

```


