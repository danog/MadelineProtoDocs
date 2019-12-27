---
title: payments.paymentReceipt
description: Receipt
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: payments.paymentReceipt  
[Back to constructors index](index.md)



Receipt

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date of generation|
|bot\_id|[int](../types/int.md) | Yes|Bot ID|
|invoice|[Invoice](../types/Invoice.md) | Yes|Invoice|
|provider\_id|[int](../types/int.md) | Yes|Provider ID|
|info|[PaymentRequestedInfo](../types/PaymentRequestedInfo.md) | Optional|Info|
|shipping|[ShippingOption](../types/ShippingOption.md) | Optional|Selected shipping option|
|currency|[string](../types/string.md) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](../types/long.md) | Yes|Total amount in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|credentials\_title|[string](../types/string.md) | Yes|Payment credential name|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [payments.PaymentReceipt](../types/payments.PaymentReceipt.md)


### Example:

```php
$payments.paymentReceipt = ['_' => 'payments.paymentReceipt', 'date' => int, 'bot_id' => int, 'invoice' => Invoice, 'provider_id' => int, 'info' => PaymentRequestedInfo, 'shipping' => ShippingOption, 'currency' => 'string', 'total_amount' => long, 'credentials_title' => 'string', 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
payments.paymentReceipt={_='payments.paymentReceipt', date=int, bot_id=int, invoice=Invoice, provider_id=int, info=PaymentRequestedInfo, shipping=ShippingOption, currency='string', total_amount=long, credentials_title='string', users={User}}

```


