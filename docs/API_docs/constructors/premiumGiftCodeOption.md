---
title: "premiumGiftCodeOption"
description: "Contains info about a giveaway/gift option."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: premiumGiftCodeOption  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [giveaway/gift](https://core.telegram.org/api/giveaways) option.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|[int](/API_docs/types/int.html) | Yes|Number of users which will be able to activate the gift codes.|
|months|[int](/API_docs/types/int.html) | Yes|Duration in months of each gifted [Telegram Premium](https://core.telegram.org/api/premium) subscription.|
|store\_product|[string](/API_docs/types/string.html) | Optional|Identifier of the store product associated with the option, official apps only.|
|store\_quantity|[int](/API_docs/types/int.html) | Optional|Number of times the store product must be paid|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|



### Type: [PremiumGiftCodeOption](/API_docs/types/PremiumGiftCodeOption.html)


### Example:

```
$premiumGiftCodeOption = ['_' => 'premiumGiftCodeOption', 'users' => int, 'months' => int, 'store_product' => 'string', 'store_quantity' => int, 'currency' => 'string', 'amount' => long];
```  
