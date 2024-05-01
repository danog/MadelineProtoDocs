---
title: "payments.paymentReceipt"
description: "Receipt"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentReceipt.html
---
# Constructor: payments.paymentReceipt  
[Back to constructors index](/API_docs/constructors/index.html)



Receipt

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](/API_docs/types/int.html) | Yes|Date of generation|
|bot\_id|[long](/API_docs/types/long.html) | Yes|Bot ID|
|provider\_id|[long](/API_docs/types/long.html) | Yes|Provider ID|
|title|[string](/API_docs/types/string.html) | Yes|Title|
|description|[string](/API_docs/types/string.html) | Yes|Description|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|Photo|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|Invoice|
|info|[PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html) | Optional|Info|
|shipping|[ShippingOption](/API_docs/types/ShippingOption.html) | Optional|Selected shipping option|
|tip\_amount|[long](/API_docs/types/long.html) | Optional|Tipped amount|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](/API_docs/types/long.html) | Yes|Total amount in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|credentials\_title|[string](/API_docs/types/string.html) | Yes|Payment credential name|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [payments.PaymentReceipt](/API_docs/types/payments.PaymentReceipt.html)


### Example:

```
$payments_paymentReceipt = ['_' => 'payments.paymentReceipt', 'date' => int, 'bot_id' => long, 'provider_id' => long, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'invoice' => Invoice, 'info' => PaymentRequestedInfo, 'shipping' => ShippingOption, 'tip_amount' => long, 'currency' => 'string', 'total_amount' => long, 'credentials_title' => 'string', 'users' => [User, User]];
```  
