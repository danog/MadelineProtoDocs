---
title: "messageActionStarGiftUnique"
description: "A gift » was upgraded to a collectible gift »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionStarGiftUnique  
[Back to constructors index](/API_docs/constructors/index.html)



A [gift »](https://core.telegram.org/api/gifts) was upgraded to a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|upgrade|[Bool](/API_docs/types/Bool.html) | Optional|If set, this collectible was [upgraded »](https://core.telegram.org/api/gifts#collectible-gifts) to a collectible gift from a previously received or sent (depending on the `out` flag of the containing [messageService](../constructors/messageService.html)) non-collectible gift.|
|transferred|[Bool](/API_docs/types/Bool.html) | Optional|If set, this collectible was transferred (either to the current user or by the current user to the other user in the private chat, depending on the `out` flag of the containing [messageService](../constructors/messageService.html)).|
|saved|[Bool](/API_docs/types/Bool.html) | Optional|If set, this gift is visible on the user or channel's profile page; can only be set for the receiver of a gift.|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|This gift was upgraded to a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts) and then re-downgraded to a regular gift because a request to refund the payment related to the upgrade was made, and the money was returned.|
|prepaid\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|The sender has pre-paid for the upgrade of this gift to a collectible gift.|
|assigned|[Bool](/API_docs/types/Bool.html) | Optional|
|from\_offer|[Bool](/API_docs/types/Bool.html) | Optional|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|The collectible gift.|
|can\_export\_at|[int](/API_docs/types/int.html) | Optional|If set, indicates that the current gift can't be [exported to the TON blockchain »](https://core.telegram.org/api/gifts#withdraw-a-collectible-gift-to-the-ton-blockchain) yet: the owner will be able to export it at the specified unixtime.|
|transfer\_stars|[long](/API_docs/types/long.html) | Optional|If set, indicates that the gift can be [transferred »](https://core.telegram.org/api/gifts#transferring-collectible-gifts) to another user by paying the specified amount of stars.|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|Sender of the gift (unset for anonymous gifts).|
|peer|[long](/API_docs/types/long.html) | Optional|Receiver of the gift.|
|saved\_id|[long](/API_docs/types/long.html) | Optional|For channel gifts, ID to use in [inputSavedStarGiftChat](../constructors/inputSavedStarGiftChat.html) constructors.|
|resale\_amount|[StarsAmount](/API_docs/types/StarsAmount.html) | Optional|Resale price of the gift.|
|can\_transfer\_at|[int](/API_docs/types/int.html) | Optional|If set, indicates that the current gift can't be [transferred »](https://core.telegram.org/api/gifts#transferring-collectible-gifts) yet: the owner will be able to transfer it at the specified unixtime.|
|can\_resell\_at|[int](/API_docs/types/int.html) | Optional|If set, indicates that the current gift can't be [resold »](https://core.telegram.org/api/gifts#reselling-collectible-gifts) yet: the owner will be able to put it up for sale at the specified unixtime.|
|drop\_original\_details\_stars|[long](/API_docs/types/long.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionStarGiftUnique = ['_' => 'messageActionStarGiftUnique', 'upgrade' => Bool, 'transferred' => Bool, 'saved' => Bool, 'refunded' => Bool, 'prepaid_upgrade' => Bool, 'assigned' => Bool, 'from_offer' => Bool, 'gift' => StarGift, 'can_export_at' => int, 'transfer_stars' => long, 'from_id' => Peer, 'peer' => long, 'saved_id' => long, 'resale_amount' => StarsAmount, 'can_transfer_at' => int, 'can_resell_at' => int, 'drop_original_details_stars' => long];
```  
