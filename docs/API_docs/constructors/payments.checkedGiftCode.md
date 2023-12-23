---
title: "payments.checkedGiftCode"
description: "payments.checkedGiftCode attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_checkedGiftCode.html
---
# Constructor: payments.checkedGiftCode  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|via\_giveaway|[Bool](/API_docs/types/Bool.html) | Optional|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|giveaway\_msg\_id|[int](/API_docs/types/int.html) | Optional|
|to\_id|[long](/API_docs/types/long.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|
|months|[int](/API_docs/types/int.html) | Yes|
|used\_date|[int](/API_docs/types/int.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.CheckedGiftCode](/API_docs/types/payments.CheckedGiftCode.html)


### Example:

```
$payments_checkedGiftCode = ['_' => 'payments.checkedGiftCode', 'via_giveaway' => Bool, 'from_id' => Peer, 'giveaway_msg_id' => int, 'to_id' => long, 'date' => int, 'months' => int, 'used_date' => int, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
