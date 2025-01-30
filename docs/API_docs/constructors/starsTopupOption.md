---
title: "starsTopupOption"
description: "Telegram Stars topup option."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsTopupOption  
[Back to constructors index](/API_docs/constructors/index.html)



[Telegram Stars topup option](https://core.telegram.org/api/stars).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|extended|[Bool](/API_docs/types/Bool.html) | Optional|If set, the option must only be shown in the full list of topup options.|
|stars|[long](/API_docs/types/long.html) | Yes|Amount of Telegram stars.|
|store\_product|[string](/API_docs/types/string.html) | Optional|Identifier of the store product associated with the option, official apps only.|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|



### Type: [StarsTopupOption](/API_docs/types/StarsTopupOption.html)


### Example:

```
$starsTopupOption = ['_' => 'starsTopupOption', 'extended' => Bool, 'stars' => long, 'store_product' => 'string', 'currency' => 'string', 'amount' => long];
```  
