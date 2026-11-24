---
title: "messageActionStarGiftOnchainOffer"
description: "messageActionStarGiftOnchainOffer attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionStarGiftOnchainOffer  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|accepted|[Bool](/API_docs/types/Bool.html) | Optional|
|declined|[Bool](/API_docs/types/Bool.html) | Optional|
|cancelled|[Bool](/API_docs/types/Bool.html) | Optional|
|expired|[Bool](/API_docs/types/Bool.html) | Optional|
|settled|[Bool](/API_docs/types/Bool.html) | Optional|
|buyer|[Bool](/API_docs/types/Bool.html) | Optional|
|cancelling|[Bool](/API_docs/types/Bool.html) | Optional|
|offer\_id|[long](/API_docs/types/long.html) | Yes|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|fee\_bps|[int](/API_docs/types/int.html) | Yes|
|expires\_at|[int](/API_docs/types/int.html) | Yes|
|offer\_address|[string](/API_docs/types/string.html) | Yes|
|buyer\_refund|[long](/API_docs/types/long.html) | Optional|
|fine|[long](/API_docs/types/long.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionStarGiftOnchainOffer = ['_' => 'messageActionStarGiftOnchainOffer', 'accepted' => Bool, 'declined' => Bool, 'cancelled' => Bool, 'expired' => Bool, 'settled' => Bool, 'buyer' => Bool, 'cancelling' => Bool, 'offer_id' => long, 'gift' => StarGift, 'amount' => long, 'fee_bps' => int, 'expires_at' => int, 'offer_address' => 'string', 'buyer_refund' => long, 'fine' => long];
```  
