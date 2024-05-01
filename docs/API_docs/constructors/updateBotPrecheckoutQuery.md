---
title: "updateBotPrecheckoutQuery"
description: "This object contains information about an incoming pre-checkout query."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotPrecheckoutQuery  
[Back to constructors index](/API_docs/constructors/index.html)



This object contains information about an incoming pre-checkout query.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](/API_docs/types/long.html) | Yes|Unique query identifier|
|user\_id|[long](/API_docs/types/long.html) | Yes|User who sent the query|
|payload|[bytes](/API_docs/types/bytes.html) | Yes|Bot specified invoice payload|
|info|[PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html) | Optional|Order info provided by the user|
|shipping\_option\_id|[string](/API_docs/types/string.html) | Optional|Identifier of the shipping option chosen by the user|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](/API_docs/types/long.html) | Yes|Total amount in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotPrecheckoutQuery = ['_' => 'updateBotPrecheckoutQuery', 'query_id' => long, 'user_id' => long, 'payload' => 'bytes', 'info' => PaymentRequestedInfo, 'shipping_option_id' => 'string', 'currency' => 'string', 'total_amount' => long];
```  
