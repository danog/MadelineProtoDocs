---
title: "payments.starsStatus"
description: "payments.starsStatus attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starsStatus.html
---
# Constructor: payments.starsStatus  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|balance|[long](/API_docs/types/long.html) | Yes|
|history|Array of [StarsTransaction](/API_docs/types/StarsTransaction.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.StarsStatus](/API_docs/types/payments.StarsStatus.html)


### Example:

```
$payments_starsStatus = ['_' => 'payments.starsStatus', 'balance' => long, 'history' => [StarsTransaction, StarsTransaction], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
