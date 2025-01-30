---
title: "messageActionPaymentSentMe"
description: "A user just sent a payment to me (a bot)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaymentSentMe  
[Back to constructors index](/API_docs/constructors/index.html)



A user just sent a payment to me (a bot)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|recurring\_init|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is the first payment of a recurring payment we just subscribed to|
|recurring\_used|[Bool](/API_docs/types/Bool.html) | Optional|Whether this payment is part of a recurring payment|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code, or `XTR` for [Telegram Stars](https://core.telegram.org/api/stars).|
|total\_amount|[long](/API_docs/types/long.html) | Yes|Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|payload|[bytes](/API_docs/types/bytes.html) | Yes|Bot specified invoice payload|
|info|[PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html) | Optional|Order info provided by the user|
|shipping\_option\_id|[string](/API_docs/types/string.html) | Optional|Identifier of the shipping option chosen by the user|
|charge|[PaymentCharge](/API_docs/types/PaymentCharge.html) | Yes|Provider payment identifier|
|subscription\_until\_date|[int](/API_docs/types/int.html) | Optional|Expiration date of the [Telegram Star subscription »](https://core.telegram.org/api/stars#star-subscriptions).|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionPaymentSentMe = ['_' => 'messageActionPaymentSentMe', 'recurring_init' => Bool, 'recurring_used' => Bool, 'currency' => 'string', 'total_amount' => long, 'payload' => 'bytes', 'info' => PaymentRequestedInfo, 'shipping_option_id' => 'string', 'charge' => PaymentCharge, 'subscription_until_date' => int];
```  
