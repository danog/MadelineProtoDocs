---
title: "payments.paymentReceipt"
description: "Receipt"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentReceipt.html
---
# Constructor: payments.paymentReceipt  
[Back to constructors index](index.md)



Receipt

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date of generation|
|bot\_id|[long](../types/long.md) | Yes|
|provider\_id|[long](../types/long.md) | Yes|
|title|[string](../types/string.md) | Yes|
|description|[string](../types/string.md) | Yes|
|photo|[WebDocument](../types/WebDocument.md) | Optional|
|invoice|[Invoice](../types/Invoice.md) | Yes|Invoice|
|info|[PaymentRequestedInfo](../types/PaymentRequestedInfo.md) | Optional|Info|
|shipping|[ShippingOption](../types/ShippingOption.md) | Optional|Selected shipping option|
|tip\_amount|[long](../types/long.md) | Optional|
|currency|[string](../types/string.md) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](../types/long.md) | Yes|Total amount in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|credentials\_title|[string](../types/string.md) | Yes|Payment credential name|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [payments.PaymentReceipt](../types/payments.PaymentReceipt.md)


### Example:

```php
$payments_paymentReceipt = ['_' => 'payments.paymentReceipt', 'date' => int, 'bot_id' => long, 'provider_id' => long, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'invoice' => Invoice, 'info' => PaymentRequestedInfo, 'shipping' => ShippingOption, 'tip_amount' => long, 'currency' => 'string', 'total_amount' => long, 'credentials_title' => 'string', 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
payments_paymentReceipt={_='payments.paymentReceipt', date=int, bot_id=long, provider_id=long, title='string', description='string', photo=WebDocument, invoice=Invoice, info=PaymentRequestedInfo, shipping=ShippingOption, tip_amount=long, currency='string', total_amount=long, credentials_title='string', users={User}}

```


