---
title: "premiumGiftOption"
description: "Telegram Premium gift option"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: premiumGiftOption  
[Back to constructors index](/API_docs/constructors/index.html)



Telegram Premium gift option

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|months|[int](/API_docs/types/int.html) | Yes|Duration of gifted Telegram Premium subscription|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|bot\_url|[string](/API_docs/types/string.html) | Yes|An [invoice deep link »](https://core.telegram.org/api/links#invoice-links) to an invoice for in-app payment, using the official Premium bot; may be empty if direct payment isn't available.|
|store\_product|[string](/API_docs/types/string.html) | Optional|An identifier for the App Store/Play Store product associated with the Premium gift.|



### Type: [PremiumGiftOption](/API_docs/types/PremiumGiftOption.html)


### Example:

```
$premiumGiftOption = ['_' => 'premiumGiftOption', 'months' => int, 'currency' => 'string', 'amount' => long, 'bot_url' => 'string', 'store_product' => 'string'];
```  
