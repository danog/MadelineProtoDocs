---
title: documentAttributeSticker
description: Document attribute sticker
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeSticker  
[Back to constructors index](index.md)



Document attribute sticker

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|mask|[Bool](../types/Bool.md) | Optional|Mask?|
|alt|[string](../types/string.md) | Yes|Alt|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|Stickerset|
|mask\_coords|[MaskCoords](../types/MaskCoords.md) | Optional|Mask coords|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeSticker = ['_' => 'documentAttributeSticker', 'mask' => Bool, 'alt' => 'string', 'stickerset' => InputStickerSet, 'mask_coords' => MaskCoords];
```  


Or, if you're into Lua:

```lua
documentAttributeSticker={_='documentAttributeSticker', mask=Bool, alt='string', stickerset=InputStickerSet, mask_coords=MaskCoords}

```


