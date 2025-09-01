---
title: "messageActionStarGift"
description: "You received a gift, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



You received a [gift, see here »](https://core.telegram.org/api/gifts) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name\_hidden|[Bool](/API_docs/types/Bool.html) | Optional|If set, the name of the sender of the gift will be hidden if the destination user decides to display the gift on their profile|
|saved|[Bool](/API_docs/types/Bool.html) | Optional|Whether this gift was added to the destination user's profile (may be toggled using [payments.saveStarGift](../methods/payments.saveStarGift.html) and fetched using [payments.getUserStarGifts](../methods/payments.getUserStarGifts.html))|
|converted|[Bool](/API_docs/types/Bool.html) | Optional|Whether this gift was converted to [Telegram Stars](https://core.telegram.org/api/stars) and cannot be displayed on the profile anymore.|
|upgraded|[Bool](/API_docs/types/Bool.html) | Optional|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|prepaid\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|upgrade\_separate|[Bool](/API_docs/types/Bool.html) | Optional|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|Info about the gift|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|Additional message from the sender of the gift|
|convert\_stars|[long](/API_docs/types/long.html) | Optional|The receiver of this gift may convert it to this many Telegram Stars, instead of displaying it on their profile page.<br>`convert_stars` will be equal to `stars` only if the gift was bought using recently bought Telegram Stars, otherwise it will be less than `stars`.|
|upgrade\_msg\_id|[int](/API_docs/types/int.html) | Optional|
|upgrade\_stars|[long](/API_docs/types/long.html) | Optional|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|peer|[long](/API_docs/types/long.html) | Optional|
|saved\_id|[long](/API_docs/types/long.html) | Optional|
|prepaid\_upgrade\_hash|[string](/API_docs/types/string.html) | Optional|
|gift\_msg\_id|[int](/API_docs/types/int.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionStarGift = ['_' => 'messageActionStarGift', 'name_hidden' => Bool, 'saved' => Bool, 'converted' => Bool, 'upgraded' => Bool, 'refunded' => Bool, 'can_upgrade' => Bool, 'prepaid_upgrade' => Bool, 'upgrade_separate' => Bool, 'gift' => StarGift, 'message' => TextWithEntities, 'convert_stars' => long, 'upgrade_msg_id' => int, 'upgrade_stars' => long, 'from_id' => Peer, 'peer' => long, 'saved_id' => long, 'prepaid_upgrade_hash' => 'string', 'gift_msg_id' => int];
```  
