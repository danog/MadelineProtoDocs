---
title: stickerSetCovered
description: Stickerset, with a specific sticker as preview
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSetCovered  
[Back to constructors index](index.md)



Stickerset, with a specific sticker as preview

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|set|[StickerSet](../types/StickerSet.md) | Yes|Stickerset|
|cover|[Document](../types/Document.md) | Optional|Preview|



### Type: [StickerSetCovered](../types/StickerSetCovered.md)


### Example:

```php
$stickerSetCovered = ['_' => 'stickerSetCovered', 'set' => StickerSet, 'cover' => Document];
```  


Or, if you're into Lua:

```lua
stickerSetCovered={_='stickerSetCovered', set=StickerSet, cover=Document}

```


