---
title: "payments.savedStarGifts"
description: "payments.savedStarGifts attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_savedStarGifts.html
---
# Constructor: payments.savedStarGifts  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|chat\_notifications\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|
|gifts|Array of [SavedStarGift](/API_docs/types/SavedStarGift.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.SavedStarGifts](/API_docs/types/payments.SavedStarGifts.html)


### Example:

```
$payments_savedStarGifts = ['_' => 'payments.savedStarGifts', 'count' => int, 'chat_notifications_enabled' => Bool, 'gifts' => [SavedStarGift, SavedStarGift], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
