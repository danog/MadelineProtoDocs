---
title: "payments.uniqueStarGift"
description: "payments.uniqueStarGift attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_uniqueStarGift.html
---
# Constructor: payments.uniqueStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.UniqueStarGift](/API_docs/types/payments.UniqueStarGift.html)


### Example:

```
$payments_uniqueStarGift = ['_' => 'payments.uniqueStarGift', 'gift' => StarGift, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
