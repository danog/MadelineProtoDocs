---
title: stickerSetCovered
description: stickerSetCovered attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetCovered  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|set|[StickerSet](../types/StickerSet.md) | Yes|
|cover|[Document](../types/Document.md) | Optional|



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


