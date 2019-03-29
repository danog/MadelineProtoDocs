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
|order|Array of [long](../types/long.md) | Yes|Order|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateStickerSetsOrder = ['_' => 'updateStickerSetsOrder', 'order' => [long, long]];
```  


Or, if you're into Lua:

```lua
updateStickerSetsOrder={_='updateStickerSetsOrder', order={long}}

```


