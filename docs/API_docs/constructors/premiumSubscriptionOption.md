---
title: "premiumSubscriptionOption"
description: "Describes a Telegram Premium subscription option"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: premiumSubscriptionOption  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a Telegram Premium subscription option

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|current|[Bool](/API_docs/types/Bool.html) | Optional|Whether this subscription option is currently in use.|
|can\_purchase\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|Whether this subscription option can be used to upgrade the existing Telegram Premium subscription. When upgrading Telegram Premium subscriptions bought through stores, make sure that the store transaction ID is equal to `transaction`, to avoid upgrading someone else's account, if the client is currently logged into multiple accounts.|
|transaction|[string](/API_docs/types/string.html) | Optional|Identifier of the last in-store transaction for the currently used subscription on the current account.|
|months|[int](/API_docs/types/int.html) | Yes|Duration of subscription in months|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|bot\_url|[string](/API_docs/types/string.html) | Yes|[Deep link](https://core.telegram.org/api/links) used to initiate payment|
|store\_product|[string](/API_docs/types/string.html) | Optional|Store product ID, only for official apps|



### Type: [PremiumSubscriptionOption](/API_docs/types/PremiumSubscriptionOption.html)


### Example:

```
$premiumSubscriptionOption = ['_' => 'premiumSubscriptionOption', 'current' => Bool, 'can_purchase_upgrade' => Bool, 'transaction' => 'string', 'months' => int, 'currency' => 'string', 'amount' => long, 'bot_url' => 'string', 'store_product' => 'string'];
```  
