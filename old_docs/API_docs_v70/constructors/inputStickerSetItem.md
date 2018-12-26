---
title: inputStickerSetItem
description: Sticker set item
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickerSetItem  
[Back to constructors index](index.md)



Sticker set item

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|document|[MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|Document|
|emoji|[string](../types/string.md) | Yes|Emoji|
|mask\_coords|[MaskCoords](../types/MaskCoords.md) | Optional|Mask coords|



### Type: [InputStickerSetItem](../types/InputStickerSetItem.md)


### Example:

```php
$inputStickerSetItem = ['_' => 'inputStickerSetItem', 'document' => InputDocument, 'emoji' => 'string', 'mask_coords' => MaskCoords];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputStickerSetItem", "document": InputDocument, "emoji": "string", "mask_coords": MaskCoords}
```


Or, if you're into Lua:

```lua
inputStickerSetItem={_='inputStickerSetItem', document=InputDocument, emoji='string', mask_coords=MaskCoords}

```


