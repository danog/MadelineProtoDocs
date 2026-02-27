---
title: "starGiftUnique"
description: "Represents a collectible star gift, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGiftUnique  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [collectible star gift, see here »](https://core.telegram.org/api/gifts#collectible-gifts) for more info.

The sticker that represents the gift is contained in a [starGiftAttributeModel](../constructors/starGiftAttributeModel.html) object in `attributes`.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|require\_premium|[Bool](/API_docs/types/Bool.html) | Optional|This gift can only be bought by users with a [Premium](https://core.telegram.org/api/premium) subscription.|
|resale\_ton\_only|[Bool](/API_docs/types/Bool.html) | Optional|Whether the gift can be bought only using Toncoins.|
|theme\_available|[Bool](/API_docs/types/Bool.html) | Optional|A chat theme associated to this gift is available, [see here »](https://core.telegram.org/api/themes#chat-themes) for more info on how to use it.|
|burned|[Bool](/API_docs/types/Bool.html) | Optional|
|crafted|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|Identifier of the collectible gift.|
|gift\_id|[long](/API_docs/types/long.html) | Yes|Unique ID of the gift.|
|title|[string](/API_docs/types/string.html) | Yes|Collectible title.|
|slug|[string](/API_docs/types/string.html) | Yes|Slug that can be used to create a [collectible gift deep link »](https://core.telegram.org/api/links#collectible-gift-link), or [elsewhere in the API where a collectible slug is accepted](https://core.telegram.org/api/gifts).|
|num|[int](/API_docs/types/int.html) | Yes|Unique identifier of this collectible gift among all (already upgraded) collectible gifts of the same type.|
|owner\_id|[Peer](/API_docs/types/Peer.html) | Optional|The owner of the gift.|
|owner\_name|[string](/API_docs/types/string.html) | Optional|The name of the owner if neither `owner_id` nor `owner_address` are set.|
|owner\_address|[string](/API_docs/types/string.html) | Optional|For [NFTs on the TON blockchain](https://core.telegram.org/api/gifts#withdraw-a-collectible-gift-to-the-ton-blockchain), contains the address of the owner (append it to the [ton\_blockchain\_explorer\_url client configuration value »](https://core.telegram.org/api/config#ton-blockchain-explorer-url) to obtain a link with information about the address).|
|attributes|Array of [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html) | Yes|Collectible attributes|
|availability\_issued|[int](/API_docs/types/int.html) | Yes|Total number of gifts of the same type that were upgraded to a collectible gift.|
|availability\_total|[int](/API_docs/types/int.html) | Yes|Total number of gifts of the same type that can be upgraded or were already upgraded to a collectible gift.|
|gift\_address|[string](/API_docs/types/string.html) | Optional|For [NFTs on the TON blockchain](https://core.telegram.org/api/gifts#withdraw-a-collectible-gift-to-the-ton-blockchain), contains the address of the NFT (append it to the [ton\_blockchain\_explorer\_url client configuration value »](https://core.telegram.org/api/config#ton-blockchain-explorer-url) to obtain a link with information about the address).|
|resell\_amount|Array of [StarsAmount](/API_docs/types/StarsAmount.html) | Optional|Resale price of the gift.|
|released\_by|[Peer](/API_docs/types/Peer.html) | Optional|This gift was released by the specified peer.|
|value\_amount|[long](/API_docs/types/long.html) | Optional|Price of the gift.|
|value\_currency|[string](/API_docs/types/string.html) | Optional|Currency for the gift's price.|
|value\_usd\_amount|[long](/API_docs/types/long.html) | Optional|
|theme\_peer|[Peer](/API_docs/types/Peer.html) | Optional|The current chat where the associated [chat theme](https://core.telegram.org/api/themes#chat-themes) is installed, if any (gift-based themes can only be installed in one chat at a time).|
|peer\_color|[PeerColor](/API_docs/types/PeerColor.html) | Optional|
|host\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|offer\_min\_stars|[int](/API_docs/types/int.html) | Optional|
|craft\_chance\_permille|[int](/API_docs/types/int.html) | Optional|



### Type: [StarGift](/API_docs/types/StarGift.html)


### Example:

```
$starGiftUnique = ['_' => 'starGiftUnique', 'require_premium' => Bool, 'resale_ton_only' => Bool, 'theme_available' => Bool, 'burned' => Bool, 'crafted' => Bool, 'id' => long, 'gift_id' => long, 'title' => 'string', 'slug' => 'string', 'num' => int, 'owner_id' => Peer, 'owner_name' => 'string', 'owner_address' => 'string', 'attributes' => [StarGiftAttribute, StarGiftAttribute], 'availability_issued' => int, 'availability_total' => int, 'gift_address' => 'string', 'resell_amount' => [StarsAmount, StarsAmount], 'released_by' => Peer, 'value_amount' => long, 'value_currency' => 'string', 'value_usd_amount' => long, 'theme_peer' => Peer, 'peer_color' => PeerColor, 'host_id' => Peer, 'offer_min_stars' => int, 'craft_chance_permille' => int];
```  
