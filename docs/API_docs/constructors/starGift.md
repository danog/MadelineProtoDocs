---
title: "starGift"
description: "Represents a star gift, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starGift  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [star gift, see here »](https://core.telegram.org/api/gifts) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|limited|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a limited-supply gift.|
|sold\_out|[Bool](/API_docs/types/Bool.html) | Optional|Whether this gift sold out and cannot be bought anymore.|
|birthday|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a birthday-themed gift|
|require\_premium|[Bool](/API_docs/types/Bool.html) | Optional|This gift can only be bought by users with a [Premium](https://core.telegram.org/api/premium) subscription.|
|limited\_per\_user|[Bool](/API_docs/types/Bool.html) | Optional|If set, the maximum number of gifts of this type that can be owned by a single user is limited and specified in `per_user_total`, and the remaining slots for the current user in `per_user_remains`.|
|peer\_color\_available|[Bool](/API_docs/types/Bool.html) | Optional|
|auction|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|Identifier of the gift|
|sticker|[Document](/API_docs/types/Document.html) | Optional|[Sticker](https://core.telegram.org/api/stickers) that represents the gift.|
|stars|[long](/API_docs/types/long.html) | Yes|Price of the gift in [Telegram Stars](https://core.telegram.org/api/stars).|
|availability\_remains|[int](/API_docs/types/int.html) | Optional|For limited-supply gifts: the remaining number of gifts that may be bought.|
|availability\_total|[int](/API_docs/types/int.html) | Optional|For limited-supply gifts: the total number of gifts that was available in the initial supply.|
|availability\_resale|[long](/API_docs/types/long.html) | Optional|The total number of (upgraded to [collectibles](https://core.telegram.org/api/gifts#collectible-gifts)) gifts of this type currently on [resale](https://core.telegram.org/api/gifts#reselling-collectible-gifts)|
|convert\_stars|[long](/API_docs/types/long.html) | Yes|The receiver of this gift may convert it to this many Telegram Stars, instead of displaying it on their profile page.<br>`convert_stars` will be equal to `stars` only if the gift was bought using recently bought Telegram Stars, otherwise it will be less than `stars`.|
|first\_sale\_date|[int](/API_docs/types/int.html) | Optional|For sold out gifts only: when was the gift first bought.|
|last\_sale\_date|[int](/API_docs/types/int.html) | Optional|For sold out gifts only: when was the gift last bought.|
|upgrade\_stars|[long](/API_docs/types/long.html) | Optional|The number of Telegram Stars the user can pay to [convert the gift into a collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).|
|resell\_min\_stars|[long](/API_docs/types/long.html) | Optional|The minimum price in [Stars](https://core.telegram.org/api/stars) for gifts of this type currently on [resale](https://core.telegram.org/api/gifts#reselling-collectible-gifts).|
|title|[string](/API_docs/types/string.html) | Optional|Title of the gift|
|released\_by|[Peer](/API_docs/types/Peer.html) | Optional|This gift was released by the specified peer.|
|per\_user\_total|[int](/API_docs/types/int.html) | Optional|Maximum number of gifts of this type that can be owned by any user.|
|per\_user\_remains|[int](/API_docs/types/int.html) | Optional|Remaining number of gifts of this type that can be owned by the current user.|
|locked\_until\_date|[int](/API_docs/types/int.html) | Optional|If set, the specified gift *possibly* cannot be sent until the specified date, see [here »](https://core.telegram.org/api/gifts) for the full flow.|
|auction\_slug|[string](/API_docs/types/string.html) | Optional|
|gifts\_per\_round|[int](/API_docs/types/int.html) | Optional|
|auction\_start\_date|[int](/API_docs/types/int.html) | Optional|
|upgrade\_variants|[int](/API_docs/types/int.html) | Optional|
|background|[StarGiftBackground](/API_docs/types/StarGiftBackground.html) | Optional|



### Type: [StarGift](/API_docs/types/StarGift.html)


### Example:

```
$starGift = ['_' => 'starGift', 'limited' => Bool, 'sold_out' => Bool, 'birthday' => Bool, 'require_premium' => Bool, 'limited_per_user' => Bool, 'peer_color_available' => Bool, 'auction' => Bool, 'id' => long, 'sticker' => Document, 'stars' => long, 'availability_remains' => int, 'availability_total' => int, 'availability_resale' => long, 'convert_stars' => long, 'first_sale_date' => int, 'last_sale_date' => int, 'upgrade_stars' => long, 'resell_min_stars' => long, 'title' => 'string', 'released_by' => Peer, 'per_user_total' => int, 'per_user_remains' => int, 'locked_until_date' => int, 'auction_slug' => 'string', 'gifts_per_round' => int, 'auction_start_date' => int, 'upgrade_variants' => int, 'background' => StarGiftBackground];
```  
