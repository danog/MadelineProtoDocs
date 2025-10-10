---
title: "payments.uniqueStarGiftValueInfo"
description: "Information about the value of a collectible gift »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_uniqueStarGiftValueInfo.html
---
# Constructor: payments.uniqueStarGiftValueInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Information about the value of a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|last\_sale\_on\_fragment|[Bool](/API_docs/types/Bool.html) | Optional|If set, the last sale was completed on Fragment.|
|value\_is\_average|[Bool](/API_docs/types/Bool.html) | Optional|If set, the `value` is calculated from the average value of sold gifts of the same type. Otherwise, it is based on the sale price of the gift.|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code (a localized fiat currency used to represent prices and price estimations in this constructor).|
|value|[long](/API_docs/types/long.html) | Yes|Estimated value of the gift, in the smallest unit of the currency specified in `currency`.|
|initial\_sale\_date|[int](/API_docs/types/int.html) | Yes|Initial purchase date of the gift.|
|initial\_sale\_stars|[long](/API_docs/types/long.html) | Yes|Initial purchase price in Stars.|
|initial\_sale\_price|[long](/API_docs/types/long.html) | Yes|Initial purchase price in the smallest unit of the currency specified in `currency` (automatically converted from `initial_sale_stars`).|
|last\_sale\_date|[int](/API_docs/types/int.html) | Optional|Last resale date of the gift.|
|last\_sale\_price|[long](/API_docs/types/long.html) | Optional|Last resale price, in the smallest unit of the currency specified in `currency`.|
|floor\_price|[long](/API_docs/types/long.html) | Optional|The current minimum price of collectible gifts of the same type, in the smallest unit of the currency specified in `currency`.|
|average\_price|[long](/API_docs/types/long.html) | Optional|The current average sale price of collectible gifts of the same type, in the smallest unit of the currency specified in `currency`.|
|listed\_count|[int](/API_docs/types/int.html) | Optional|Number of gifts of the same type currently being resold on Telegram.|
|fragment\_listed\_count|[int](/API_docs/types/int.html) | Optional|Number of gifts of the same type currently being resold on fragment.|
|fragment\_listed\_url|[string](/API_docs/types/string.html) | Optional|Fragment link to the listing of gifts of the same type currently being resold on fragment.|



### Type: [payments.UniqueStarGiftValueInfo](/API_docs/types/payments.UniqueStarGiftValueInfo.html)


### Example:

```
$payments_uniqueStarGiftValueInfo = ['_' => 'payments.uniqueStarGiftValueInfo', 'last_sale_on_fragment' => Bool, 'value_is_average' => Bool, 'currency' => 'string', 'value' => long, 'initial_sale_date' => int, 'initial_sale_stars' => long, 'initial_sale_price' => long, 'last_sale_date' => int, 'last_sale_price' => long, 'floor_price' => long, 'average_price' => long, 'listed_count' => int, 'fragment_listed_count' => int, 'fragment_listed_url' => 'string'];
```  
