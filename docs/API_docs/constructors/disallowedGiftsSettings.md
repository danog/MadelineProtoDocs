---
title: "disallowedGiftsSettings"
description: "Disallow the reception of specific gift types."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: disallowedGiftsSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Disallow the reception of specific [gift](https://core.telegram.org/api/gifts) types.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|disallow\_unlimited\_stargifts|[Bool](/API_docs/types/Bool.html) | Optional|Disallow the reception of gifts with an unlimited supply (those with the [starGift](../constructors/starGift.html).`limited` flag **not** set).|
|disallow\_limited\_stargifts|[Bool](/API_docs/types/Bool.html) | Optional|Disallow the reception of limited-supply gifts (those with the [starGift](../constructors/starGift.html).`limited` flag set).|
|disallow\_unique\_stargifts|[Bool](/API_docs/types/Bool.html) | Optional|Disallow the reception of [collectible gifts »](https://core.telegram.org/api/gifts#collectible-gifts).|
|disallow\_premium\_gifts|[Bool](/API_docs/types/Bool.html) | Optional|Disallow the reception of [gifted Telegram Premium subscriptions »](https://core.telegram.org/api/gifts#collectible-gifts).|
|disallow\_stargifts\_from\_channels|[Bool](/API_docs/types/Bool.html) | Optional|



### Type: [DisallowedGiftsSettings](/API_docs/types/DisallowedGiftsSettings.html)


### Example:

```
$disallowedGiftsSettings = ['_' => 'disallowedGiftsSettings', 'disallow_unlimited_stargifts' => Bool, 'disallow_limited_stargifts' => Bool, 'disallow_unique_stargifts' => Bool, 'disallow_premium_gifts' => Bool, 'disallow_stargifts_from_channels' => Bool];
```  
