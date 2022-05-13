---
title: "inputStickerSetItem"
description: "Sticker in a stickerset"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetItem  
[Back to constructors index](/API_docs/constructors/index.html)



Sticker in a stickerset

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|The sticker|
|emoji|[string](/API_docs/types/string.html) | Yes|Associated emoji|
|mask\_coords|[MaskCoords](/API_docs/types/MaskCoords.html) | Optional|Coordinates for mask sticker|



### Type: [InputStickerSetItem](/API_docs/types/InputStickerSetItem.html)


### Example:

```
$inputStickerSetItem = ['_' => 'inputStickerSetItem', 'document' => InputDocument, 'emoji' => 'string', 'mask_coords' => MaskCoords];
```  
