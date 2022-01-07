---
title: "documentAttributeSticker"
description: "Defines a sticker"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeSticker  
[Back to constructors index](/API_docs/constructors/index.md)



Defines a sticker

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|mask|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is a mask sticker|
|alt|[string](/API_docs/types/string.md) | Yes|Alternative emoji representation of sticker|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.md) | Optional|Associated stickerset|
|mask\_coords|[MaskCoords](/API_docs/types/MaskCoords.md) | Optional|Mask coordinates (if this is a mask sticker, attached to a photo)|



### Type: [DocumentAttribute](/API_docs/types/DocumentAttribute.md)


### Example:

```php
$documentAttributeSticker = ['_' => 'documentAttributeSticker', 'mask' => Bool, 'alt' => 'string', 'stickerset' => InputStickerSet, 'mask_coords' => MaskCoords];
```  
