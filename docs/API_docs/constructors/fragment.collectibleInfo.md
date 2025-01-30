---
title: "fragment.collectibleInfo"
description: "Info about a fragment collectible."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/fragment_collectibleInfo.html
---
# Constructor: fragment.collectibleInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a [fragment collectible](https://core.telegram.org/api/fragment).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|purchase\_date|[int](/API_docs/types/int.html) | Yes|Purchase date (unixtime)|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code for `amount`|
|amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|crypto\_currency|[string](/API_docs/types/string.html) | Yes|Cryptocurrency name.|
|crypto\_amount|[long](/API_docs/types/long.html) | Yes|Price, in the smallest units of the cryptocurrency.|
|url|[string](/API_docs/types/string.html) | Yes|[Fragment](https://fragment.com) URL with more info about the collectible|



### Type: [fragment.CollectibleInfo](/API_docs/types/fragment.CollectibleInfo.html)


### Example:

```
$fragment_collectibleInfo = ['_' => 'fragment.collectibleInfo', 'purchase_date' => int, 'currency' => 'string', 'amount' => long, 'crypto_currency' => 'string', 'crypto_amount' => long, 'url' => 'string'];
```  
