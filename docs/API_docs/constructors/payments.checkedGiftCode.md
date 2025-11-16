---
title: "payments.checkedGiftCode"
description: "Contains info about a Telegram Premium giftcode link."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_checkedGiftCode.html
---
# Constructor: payments.checkedGiftCode  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [Telegram Premium giftcode link](https://core.telegram.org/api/links#premium-giftcode-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|via\_giveaway|[Bool](/API_docs/types/Bool.html) | Optional|Whether this giftcode was created by a [giveaway](https://core.telegram.org/api/giveaways).|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|The peer that created the gift code.|
|giveaway\_msg\_id|[int](/API_docs/types/int.html) | Optional|Message ID of the giveaway in the channel specified in `from_id`.|
|to\_id|[long](/API_docs/types/long.html) | Optional|The destination user of the gift.|
|date|[int](/API_docs/types/int.html) | Yes|Creation date of the gift code.|
|days|[int](/API_docs/types/int.html) | Yes|
|used\_date|[int](/API_docs/types/int.html) | Optional|When was the giftcode imported, if it was imported.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [payments.CheckedGiftCode](/API_docs/types/payments.CheckedGiftCode.html)


### Example:

```
$payments_checkedGiftCode = ['_' => 'payments.checkedGiftCode', 'via_giveaway' => Bool, 'from_id' => Peer, 'giveaway_msg_id' => int, 'to_id' => long, 'date' => int, 'days' => int, 'used_date' => int, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
