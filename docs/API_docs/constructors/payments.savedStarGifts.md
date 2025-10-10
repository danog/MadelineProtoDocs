---
title: "payments.savedStarGifts"
description: "Represents a list of gifts."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_savedStarGifts.html
---
# Constructor: payments.savedStarGifts  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a list of [gifts](https://core.telegram.org/api/gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results (can be less than the returned `gifts`, in which case `next_offset` will be set).|
|chat\_notifications\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|Ternary value: can be not set, set&amp;true, set&amp;false. <br>Can only be set for channels we own: the value indicates whether we [enabled gift notifications](https://core.telegram.org/api/gifts#notifications-for-received-channel-gifts) for this channel.|
|gifts|Array of [SavedStarGift](/API_docs/types/SavedStarGift.html) | Yes|Gifts|
|next\_offset|[string](/API_docs/types/string.html) | Optional|Offset to pass to [payments.getSavedStarGifts](../methods/payments.getSavedStarGifts.html) to fetch the next page of results.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Channels mentioned in `gifts`|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in `gifts`|



### Type: [payments.SavedStarGifts](/API_docs/types/payments.SavedStarGifts.html)


### Example:

```
$payments_savedStarGifts = ['_' => 'payments.savedStarGifts', 'count' => int, 'chat_notifications_enabled' => Bool, 'gifts' => [SavedStarGift, SavedStarGift], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
