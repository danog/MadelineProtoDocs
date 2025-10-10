---
title: "payments.resaleStarGifts"
description: "List of gifts currently on resale »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_resaleStarGifts.html
---
# Constructor: payments.resaleStarGifts  
[Back to constructors index](/API_docs/constructors/index.html)



List of gifts currently on [resale »](https://core.telegram.org/api/gifts#reselling-collectible-gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results.|
|gifts|Array of [StarGift](/API_docs/types/StarGift.html) | Yes|Collectible gifts on resale (may be less than `count`, in which case `next_offset` will be set).|
|next\_offset|[string](/API_docs/types/string.html) | Optional|Offset for pagination, pass this to [payments.getResaleStarGifts](../methods/payments.getResaleStarGifts.html).`offset` to fetch the next results.|
|attributes|Array of [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html) | Optional|Possible gift attributes, only set if [payments.getResaleStarGifts](../methods/payments.getResaleStarGifts.html).`attributes_hash` is set (on the first call, it must be equal to `0`).|
|attributes\_hash|[long](/API_docs/types/long.html) | Optional|Hash of the `attributes` field, pass this to [payments.getResaleStarGifts](../methods/payments.getResaleStarGifts.html).`attributes_hash` to avoid returning any attributes (flag not set) if they haven't changed.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in the attributes.|
|counters|Array of [StarGiftAttributeCounter](/API_docs/types/StarGiftAttributeCounter.html) | Optional|Indicates the total number of gifts that have a specific attribute, only set if [payments.getResaleStarGifts](../methods/payments.getResaleStarGifts.html).`offset` is empty (since this field is not related to the current result page but to all of them, it's only returned on the first page).|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the attributes.|



### Type: [payments.ResaleStarGifts](/API_docs/types/payments.ResaleStarGifts.html)


### Example:

```
$payments_resaleStarGifts = ['_' => 'payments.resaleStarGifts', 'count' => int, 'gifts' => [StarGift, StarGift], 'next_offset' => 'string', 'attributes' => [StarGiftAttribute, StarGiftAttribute], 'attributes_hash' => long, 'chats' => [Chat, Chat], 'counters' => [StarGiftAttributeCounter, StarGiftAttributeCounter], 'users' => [User, User]];
```  
