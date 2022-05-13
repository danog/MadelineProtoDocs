---
title: "documentAttributeSticker"
description: "Defines a sticker"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: documentAttributeSticker  
[Back to constructors index](/API_docs/constructors/index.html)



Defines a sticker

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|mask|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a mask sticker|
|alt|[string](/API_docs/types/string.html) | Yes|Alternative emoji representation of sticker|
|stickerset|[InputStickerSet](/API_docs/types/InputStickerSet.html) | Optional|Associated stickerset|
|mask\_coords|[MaskCoords](/API_docs/types/MaskCoords.html) | Optional|Mask coordinates (if this is a mask sticker, attached to a photo)|



### Type: [DocumentAttribute](/API_docs/types/DocumentAttribute.html)


### Example:

```
$documentAttributeSticker = ['_' => 'documentAttributeSticker', 'mask' => Bool, 'alt' => 'string', 'stickerset' => InputStickerSet, 'mask_coords' => MaskCoords];
```  
