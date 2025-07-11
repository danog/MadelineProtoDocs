---
title: "payments.starGifts"
description: "Available gifts »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGifts.html
---
# Constructor: payments.starGifts  
[Back to constructors index](/API_docs/constructors/index.html)



Available [gifts »](https://core.telegram.org/api/gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](/API_docs/types/int.html) | Yes|
|gifts|Array of [StarGift](/API_docs/types/StarGift.html) | Yes|List of available gifts.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.StarGifts](/API_docs/types/payments.StarGifts.html)


### Example:

```
$payments_starGifts = ['_' => 'payments.starGifts', 'hash' => int, 'gifts' => [StarGift, StarGift], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
