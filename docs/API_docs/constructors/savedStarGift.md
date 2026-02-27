---
title: "savedStarGift"
description: "Represents a gift owned by a peer."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: savedStarGift  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [gift](https://core.telegram.org/api/gifts) owned by a peer.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name\_hidden|[Bool](/API_docs/types/Bool.html) | Optional|If set, the gift sender in `from_id` and the `message` are set only for the receiver of the gift.|
|unsaved|[Bool](/API_docs/types/Bool.html) | Optional|If set, the gift is **not** pinned on the user's profile.|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|This gift was upgraded to a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts) and then re-downgraded to a regular gift because a request to refund the payment related to the upgrade was made, and the money was returned.|
|can\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|Only set for non-collectible gifts, if they can be upgraded to a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).|
|pinned\_to\_top|[Bool](/API_docs/types/Bool.html) | Optional|Whether this gift is pinned on top of the user's profile page.|
|upgrade\_separate|[Bool](/API_docs/types/Bool.html) | Optional|If set, someone already [separately pre-paid](https://core.telegram.org/api/gifts#prepaying-for-someone-elses-upgrade) for the upgrade of this gift.|
|from\_id|[Peer](/API_docs/types/Peer.html) | Optional|Sender of the gift (unset for anonymous gifts).|
|date|[int](/API_docs/types/int.html) | Yes|Reception date of the gift.|
|gift|[StarGift](/API_docs/types/StarGift.html) | Yes|The collectible gift.|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Optional|Message attached to the gift.|
|msg\_id|[int](/API_docs/types/int.html) | Optional|For gifts received by users, ID to use in [inputSavedStarGiftUser](../constructors/inputSavedStarGiftUser.html) constructors.|
|saved\_id|[long](/API_docs/types/long.html) | Optional|For gifts received by channels, ID to use in [inputSavedStarGiftChat](../constructors/inputSavedStarGiftChat.html) constructors.|
|convert\_stars|[long](/API_docs/types/long.html) | Optional|For non-collectible gifts, the receiver of this gift may convert it to this many Telegram Stars, instead of displaying it on their profile page.|
|upgrade\_stars|[long](/API_docs/types/long.html) | Optional|**Only** for **pre-paid** non-collectible gifts, the number of Telegram Stars the sender has **already paid** to [convert the gift into a collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts) (this is different from the meaning of the flag in [messageActionStarGift](../constructors/messageActionStarGift.html), where it signals the upgrade price for not yet upgraded gifts).|
|can\_export\_at|[int](/API_docs/types/int.html) | Optional|If set, indicates that the current gift can't be [exported to the TON blockchain »](https://core.telegram.org/api/gifts#withdraw-a-collectible-gift-to-the-ton-blockchain) yet: the owner will be able to export it at the specified unixtime.|
|transfer\_stars|[long](/API_docs/types/long.html) | Optional|If set, indicates that the gift can be [transferred »](https://core.telegram.org/api/gifts#transferring-collectible-gifts) to another user by paying the specified amount of stars.|
|can\_transfer\_at|[int](/API_docs/types/int.html) | Optional|If set, indicates that the current gift can't be [transferred »](https://core.telegram.org/api/gifts#transferring-collectible-gifts) yet: the owner will be able to transfer it at the specified unixtime.|
|can\_resell\_at|[int](/API_docs/types/int.html) | Optional|If set, indicates that the current gift can't be [resold »](https://core.telegram.org/api/gifts#reselling-collectible-gifts) yet: the owner will be able to put it up for sale at the specified unixtime.|
|collection\_id|Array of [int](/API_docs/types/int.html) | Optional|IDs of the [collections »](https://core.telegram.org/api/gifts#gift-collections) that this gift is a part of.|
|prepaid\_upgrade\_hash|[string](/API_docs/types/string.html) | Optional|[Hash to prepay for a gift upgrade separately »](https://core.telegram.org/api/gifts#prepaying-for-someone-elses-upgrade).|
|drop\_original\_details\_stars|[long](/API_docs/types/long.html) | Optional|
|gift\_num|[int](/API_docs/types/int.html) | Optional|
|can\_craft\_at|[int](/API_docs/types/int.html) | Optional|



### Type: [SavedStarGift](/API_docs/types/SavedStarGift.html)


### Example:

```
$savedStarGift = ['_' => 'savedStarGift', 'name_hidden' => Bool, 'unsaved' => Bool, 'refunded' => Bool, 'can_upgrade' => Bool, 'pinned_to_top' => Bool, 'upgrade_separate' => Bool, 'from_id' => Peer, 'date' => int, 'gift' => StarGift, 'message' => TextWithEntities, 'msg_id' => int, 'saved_id' => long, 'convert_stars' => long, 'upgrade_stars' => long, 'can_export_at' => int, 'transfer_stars' => long, 'can_transfer_at' => int, 'can_resell_at' => int, 'collection_id' => [int, int], 'prepaid_upgrade_hash' => 'string', 'drop_original_details_stars' => long, 'gift_num' => int, 'can_craft_at' => int];
```  
