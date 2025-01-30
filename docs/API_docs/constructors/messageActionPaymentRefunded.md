---
title: "messageActionPaymentRefunded"
description: "Describes a payment refund (service message received by both users and bots)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaymentRefunded  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a payment refund (service message received by both users and bots).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Identifier of the peer that returned the funds.|
|currency|[string](/API_docs/types/string.html) | Yes|Currency, `XTR` for Telegram Stars.|
|total\_amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|payload|[bytes](/API_docs/types/bytes.html) | Optional|Bot specified invoice payload (only received by bots).|
|charge|[PaymentCharge](/API_docs/types/PaymentCharge.html) | Yes|Provider payment identifier|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionPaymentRefunded = ['_' => 'messageActionPaymentRefunded', 'peer' => long, 'currency' => 'string', 'total_amount' => long, 'payload' => 'bytes', 'charge' => PaymentCharge];
```  
