---
title: "updateStickerSetsOrder"
description: "The order of stickersets was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateStickerSetsOrder  
[Back to constructors index](/API_docs/constructors/index.html)



The order of stickersets was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|masks|[Bool](/API_docs/types/Bool.html) | Optional|Whether the updated stickers are mask stickers|
|order|Array of [long](/API_docs/types/long.html) | Yes|New sticker order by sticker ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateStickerSetsOrder = ['_' => 'updateStickerSetsOrder', 'masks' => Bool, 'order' => [long, long]];
```  
