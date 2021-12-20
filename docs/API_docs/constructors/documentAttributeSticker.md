---
title: "documentAttributeSticker"
description: "Defines a sticker"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeSticker  
[Back to constructors index](index.md)



Defines a sticker

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|mask|[Bool](../types/Bool.md) | Optional|Whether this is a mask sticker|
|alt|[string](../types/string.md) | Yes|Alternative emoji representation of sticker|
|stickerset|[InputStickerSet](../types/InputStickerSet.md) | Optional|Associated stickerset|
|mask\_coords|[MaskCoords](../types/MaskCoords.md) | Optional|Mask coordinates (if this is a mask sticker, attached to a photo)|



### Type: [DocumentAttribute](../types/DocumentAttribute.md)


### Example:

```php
$documentAttributeSticker = ['_' => 'documentAttributeSticker', 'mask' => Bool, 'alt' => 'string', 'stickerset' => InputStickerSet, 'mask_coords' => MaskCoords];
```  


Or, if you're into Lua:

```lua
documentAttributeSticker={_='documentAttributeSticker', mask=Bool, alt='string', stickerset=InputStickerSet, mask_coords=MaskCoords}

```


