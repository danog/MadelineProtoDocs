---
title: "inputStickerSetItem"
description: "Sticker in a stickerset"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetItem  
[Back to constructors index](/API_docs/constructors/index.md)



Sticker in a stickerset

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.md) | Optional|The sticker|
|emoji|[string](/API_docs/types/string.md) | Yes|Associated emoji|
|mask\_coords|[MaskCoords](/API_docs/types/MaskCoords.md) | Optional|Coordinates for mask sticker|



### Type: [InputStickerSetItem](/API_docs/types/InputStickerSetItem.md)


### Example:

```php
$inputStickerSetItem = ['_' => 'inputStickerSetItem', 'document' => InputDocument, 'emoji' => 'string', 'mask_coords' => MaskCoords];
```  
