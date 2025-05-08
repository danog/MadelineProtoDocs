---
title: "payments.resaleStarGifts"
description: "payments.resaleStarGifts attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_resaleStarGifts.html
---
# Constructor: payments.resaleStarGifts  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|gifts|Array of [StarGift](/API_docs/types/StarGift.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|attributes|Array of [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html) | Optional|
|attributes\_hash|[long](/API_docs/types/long.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|counters|Array of [StarGiftAttributeCounter](/API_docs/types/StarGiftAttributeCounter.html) | Optional|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.ResaleStarGifts](/API_docs/types/payments.ResaleStarGifts.html)


### Example:

```
$payments_resaleStarGifts = ['_' => 'payments.resaleStarGifts', 'count' => int, 'gifts' => [StarGift, StarGift], 'next_offset' => 'string', 'attributes' => [StarGiftAttribute, StarGiftAttribute], 'attributes_hash' => long, 'chats' => [Chat, Chat], 'counters' => [StarGiftAttributeCounter, StarGiftAttributeCounter], 'users' => [User, User]];
```  
