---
title: "payments.starGiftActiveAuctions"
description: "payments.starGiftActiveAuctions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGiftActiveAuctions.html
---
# Constructor: payments.starGiftActiveAuctions  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|auctions|Array of [StarGiftActiveAuctionState](/API_docs/types/StarGiftActiveAuctionState.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|



### Type: [payments.StarGiftActiveAuctions](/API_docs/types/payments.StarGiftActiveAuctions.html)


### Example:

```
$payments_starGiftActiveAuctions = ['_' => 'payments.starGiftActiveAuctions', 'auctions' => [StarGiftActiveAuctionState, StarGiftActiveAuctionState], 'users' => [User, User], 'chats' => [Chat, Chat]];
```  
