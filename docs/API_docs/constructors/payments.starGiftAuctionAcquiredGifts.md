---
title: "payments.starGiftAuctionAcquiredGifts"
description: "payments.starGiftAuctionAcquiredGifts attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGiftAuctionAcquiredGifts.html
---
# Constructor: payments.starGiftAuctionAcquiredGifts  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gifts|Array of [StarGiftAuctionAcquiredGift](/API_docs/types/StarGiftAuctionAcquiredGift.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|



### Type: [payments.StarGiftAuctionAcquiredGifts](/API_docs/types/payments.StarGiftAuctionAcquiredGifts.html)


### Example:

```
$payments_starGiftAuctionAcquiredGifts = ['_' => 'payments.starGiftAuctionAcquiredGifts', 'gifts' => [StarGiftAuctionAcquiredGift, StarGiftAuctionAcquiredGift], 'users' => [User, User], 'chats' => [Chat, Chat]];
```  
