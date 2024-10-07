---
title: "payments.userStarGifts"
description: "payments.userStarGifts attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_userStarGifts.html
---
# Constructor: payments.userStarGifts  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|gifts|Array of [UserStarGift](/API_docs/types/UserStarGift.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.UserStarGifts](/API_docs/types/payments.UserStarGifts.html)


### Example:

```
$payments_userStarGifts = ['_' => 'payments.userStarGifts', 'count' => int, 'gifts' => [UserStarGift, UserStarGift], 'next_offset' => 'string', 'users' => [User, User]];
```  
