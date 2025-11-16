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
|saved|[Bool](/API_docs/types/Bool.html) | Optional|Whether this gift was added to the destination user's profile (may be toggled using [payments.saveStarGift](../methods/payments.saveStarGift.html) and fetched using [payments.getSavedStarGifts](../methods/payments.getSavedStarGifts.html))|
|converted|[Bool](/API_docs/types/Bool.html) | Optional|Whether this gift was converted to [Telegram Stars](https://core.telegram.org/api/stars) and cannot be displayed on the profile anymore.|
|upgraded|[Bool](/API_docs/types/Bool.html) | Optional|This gift was upgraded to a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|This gift is not available anymore because a request to refund the payment related to this gift was made, and the money was returned.|
|can\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|If set, this gift can be [upgraded to a collectible gift](https://core.telegram.org/api/gifts#upgrade-a-gift-to-a-collectible-gift); can only be set for the receiver of a gift.|
|prepaid\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|The sender has already pre-paid for the upgrade of this gift to a collectible gift.|
|upgrade\_separate|[Bool](/API_docs/types/Bool.html) | Optional|This service message is the notification of a [separate pre-payment for the upgrade of a gift we own](https://core.telegram.org/api/gifts#prepaying-for-someone-elses-upgrade).|
|auction\_acquired|[Bool](/API_docs/types/Bool.html) | Optional|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|Info about the gift|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|Additional message from the sender of the gift|
|convert\_stars|[long](/API_docs/types/long.html) | Optional|The receiver of this gift may convert it to this many Telegram Stars, instead of displaying it on their profile page.<br>`convert_stars` will be equal to `stars` only if the gift was bought using recently bought Telegram Stars, otherwise it will be less than `stars`.|
|upgrade\_msg\_id|[int](/API_docs/types/int.html) | Optional|If set, this gift was [upgraded to a collectible gift](https://core.telegram.org/api/gifts#upgrade-a-gift-to-a-collectible-gift), and the corresponding [messageActionStarGiftUnique](../constructors/messageActionStarGiftUnique.html) is available at the specified message ID.|
|upgrade\_stars|[long](/API_docs/types/long.html) | Optional|The number of Telegram Stars the user can pay to [convert the gift into a collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|Sender of the gift (unset for anonymous gifts).|
|peer|[long](/API_docs/types/long.html) | Optional|Receiver of the gift.|
|saved\_id|[long](/API_docs/types/long.html) | Optional|For channel gifts, ID to use in [inputSavedStarGiftChat](../constructors/inputSavedStarGiftChat.html) constructors.|
|prepaid\_upgrade\_hash|[string](/API_docs/types/string.html) | Optional|[Hash to prepay for a gift upgrade separately »](https://core.telegram.org/api/gifts#prepaying-for-someone-elses-upgrade).|
|gift\_msg\_id|[int](/API_docs/types/int.html) | Optional|For [separate upgrades](https://core.telegram.org/api/gifts#prepaying-for-someone-elses-upgrade), the identifier of the message with the gift whose upgrade was prepaid (only valid for the receiver of the service message).|
|to\_id|[Peer](/API_docs/types/Peer.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionStarGift = ['_' => 'messageActionStarGift', 'name_hidden' => Bool, 'saved' => Bool, 'converted' => Bool, 'upgraded' => Bool, 'refunded' => Bool, 'can_upgrade' => Bool, 'prepaid_upgrade' => Bool, 'upgrade_separate' => Bool, 'auction_acquired' => Bool, 'gift' => StarGift, 'message' => TextWithEntities, 'convert_stars' => long, 'upgrade_msg_id' => int, 'upgrade_stars' => long, 'from_id' => Peer, 'peer' => long, 'saved_id' => long, 'prepaid_upgrade_hash' => 'string', 'gift_msg_id' => int, 'to_id' => Peer];
```  
