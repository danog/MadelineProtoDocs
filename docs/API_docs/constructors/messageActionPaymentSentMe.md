---
title: "messageActionPaymentSentMe"
description: "A user just sent a payment to me (a bot)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaymentSentMe  
[Back to constructors index](/API_docs/constructors/index.md)



A user just sent a payment to me (a bot)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|currency|[string](/API_docs/types/string.md) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](/API_docs/types/long.md) | Yes|Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|payload|[bytes](/API_docs/types/bytes.md) | Yes|Bot specified invoice payload|
|info|[PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.md) | Optional|Order info provided by the user|
|shipping\_option\_id|[string](/API_docs/types/string.md) | Optional|Identifier of the shipping option chosen by the user|
|charge|[PaymentCharge](/API_docs/types/PaymentCharge.md) | Yes|Provider payment identifier|



### Type: [MessageAction](/API_docs/types/MessageAction.md)


### Example:

```php
$messageActionPaymentSentMe = ['_' => 'messageActionPaymentSentMe', 'currency' => 'string', 'total_amount' => long, 'payload' => 'bytes', 'info' => PaymentRequestedInfo, 'shipping_option_id' => 'string', 'charge' => PaymentCharge];
```  
