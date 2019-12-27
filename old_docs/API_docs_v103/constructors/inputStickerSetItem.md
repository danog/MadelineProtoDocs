---
title: inputStickerSetItem
description: Sticker in a stickerset
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetItem  
[Back to constructors index](index.md)



Sticker in a stickerset

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document|[MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|The sticker|
|emoji|[string](../types/string.md) | Yes|Associated emoji|
|mask\_coords|[MaskCoords](../types/MaskCoords.md) | Optional|Coordinates for mask sticker|



### Type: [InputStickerSetItem](../types/InputStickerSetItem.md)


### Example:

```php
$inputStickerSetItem = ['_' => 'inputStickerSetItem', 'document' => InputDocument, 'emoji' => 'string', 'mask_coords' => MaskCoords];
```  


Or, if you're into Lua:

```lua
inputStickerSetItem={_='inputStickerSetItem', document=InputDocument, emoji='string', mask_coords=MaskCoords}

```


