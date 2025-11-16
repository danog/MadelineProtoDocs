---
title: "payments.starGiftAuctionState"
description: "payments.starGiftAuctionState attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGiftAuctionState.html
---
# Constructor: payments.starGiftAuctionState  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|state|[StarGiftAuctionState](/API_docs/types/StarGiftAuctionState.html) | Yes|
|user\_state|[StarGiftAuctionUserState](/API_docs/types/StarGiftAuctionUserState.html) | Yes|
|timeout|[int](/API_docs/types/int.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.StarGiftAuctionState](/API_docs/types/payments.StarGiftAuctionState.html)


### Example:

```
$payments_starGiftAuctionState = ['_' => 'payments.starGiftAuctionState', 'gift' => StarGift, 'state' => StarGiftAuctionState, 'user_state' => StarGiftAuctionUserState, 'timeout' => int, 'users' => [User, User]];
```  
