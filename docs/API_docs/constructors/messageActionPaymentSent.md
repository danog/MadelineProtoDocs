---
title: "messageActionPaymentSent"
description: "A payment was sent"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaymentSent  
[Back to constructors index](/API_docs/constructors/index.html)



A payment was sent

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|recurring\_init|[Bool](/API_docs/types/Bool.html) | Optional|
|recurring\_used|[Bool](/API_docs/types/Bool.html) | Optional|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](/API_docs/types/long.html) | Yes|Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|invoice\_slug|[string](/API_docs/types/string.html) | Optional|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionPaymentSent = ['_' => 'messageActionPaymentSent', 'recurring_init' => Bool, 'recurring_used' => Bool, 'currency' => 'string', 'total_amount' => long, 'invoice_slug' => 'string'];
```  
