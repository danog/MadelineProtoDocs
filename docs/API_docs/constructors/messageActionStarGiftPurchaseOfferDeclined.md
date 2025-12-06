---
title: "messageActionStarGiftPurchaseOfferDeclined"
description: "messageActionStarGiftPurchaseOfferDeclined attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionStarGiftPurchaseOfferDeclined  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|expired|[Bool](/API_docs/types/Bool.html) | Optional|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|price|[StarsAmount](/API_docs/types/StarsAmount.html) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionStarGiftPurchaseOfferDeclined = ['_' => 'messageActionStarGiftPurchaseOfferDeclined', 'expired' => Bool, 'gift' => StarGift, 'price' => StarsAmount];
```  
