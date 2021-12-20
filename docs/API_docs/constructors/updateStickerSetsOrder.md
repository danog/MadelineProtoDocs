---
title: "updateStickerSetsOrder"
description: "The order of stickersets was changed"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateStickerSetsOrder  
[Back to constructors index](index.md)



The order of stickersets was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|masks|[Bool](../types/Bool.md) | Optional|Whether the updated stickers are mask stickers|
|order|Array of [long](../types/long.md) | Yes|New sticker order by sticker ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateStickerSetsOrder = ['_' => 'updateStickerSetsOrder', 'masks' => Bool, 'order' => [long, long]];
```  


Or, if you're into Lua:

```lua
updateStickerSetsOrder={_='updateStickerSetsOrder', masks=Bool, order={long}}

```


