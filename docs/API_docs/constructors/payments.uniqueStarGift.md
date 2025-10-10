---
title: "payments.uniqueStarGift"
description: "Represents a collectible gift »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_uniqueStarGift.html
---
# Constructor: payments.uniqueStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|The [starGiftUnique](../constructors/starGiftUnique.html) constructor.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in the `gift` field.|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the `gift` field.|



### Type: [payments.UniqueStarGift](/API_docs/types/payments.UniqueStarGift.html)


### Example:

```
$payments_uniqueStarGift = ['_' => 'payments.uniqueStarGift', 'gift' => StarGift, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
