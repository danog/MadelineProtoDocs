---
title: "messageActionStarGiftPurchaseOffer"
description: "messageActionStarGiftPurchaseOffer attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionStarGiftPurchaseOffer  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|accepted|[Bool](/API_docs/types/Bool.html) | Optional|
|declined|[Bool](/API_docs/types/Bool.html) | Optional|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|price|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|
|expires\_at|[int](/API_docs/types/int.html) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionStarGiftPurchaseOffer = ['_' => 'messageActionStarGiftPurchaseOffer', 'accepted' => Bool, 'declined' => Bool, 'gift' => StarGift, 'price' => StarsAmount, 'expires_at' => int];
```  
