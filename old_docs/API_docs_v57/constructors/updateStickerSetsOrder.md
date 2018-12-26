---
title: updateStickerSetsOrder
description: Update sticker sets order
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateStickerSetsOrder  
[Back to constructors index](index.md)



Update sticker sets order

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|masks|[Bool](../types/Bool.md) | Optional|Masks?|
|order|Array of [long](../types/long.md) | Yes|Order|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateStickerSetsOrder = ['_' => 'updateStickerSetsOrder', 'masks' => Bool, 'order' => [long, long]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateStickerSetsOrder", "masks": Bool, "order": [long]}
```


Or, if you're into Lua:

```lua
updateStickerSetsOrder={_='updateStickerSetsOrder', masks=Bool, order={long}}

```


