---
title: payments.paymentReceipt
description: Payment receipt
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: payments.paymentReceipt  
[Back to constructors index](index.md)



Payment receipt

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date|
|bot\_id|[int](../types/int.md) | Yes|Bot ID|
|invoice|[Invoice](../types/Invoice.md) | Yes|Invoice|
|provider\_id|[int](../types/int.md) | Yes|Provider ID|
|info|[PaymentRequestedInfo](../types/PaymentRequestedInfo.md) | Optional|Info|
|shipping|[ShippingOption](../types/ShippingOption.md) | Optional|Shipping|
|currency|[string](../types/string.md) | Yes|Currency|
|total\_amount|[long](../types/long.md) | Yes|Total amount|
|credentials\_title|[string](../types/string.md) | Yes|Credentials title|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [payments\_PaymentReceipt](../types/payments_PaymentReceipt.md)


### Example:

```php
$payments_paymentReceipt = ['_' => 'payments.paymentReceipt', 'date' => int, 'bot_id' => int, 'invoice' => Invoice, 'provider_id' => int, 'info' => PaymentRequestedInfo, 'shipping' => ShippingOption, 'currency' => 'string', 'total_amount' => long, 'credentials_title' => 'string', 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "payments.paymentReceipt", "date": int, "bot_id": int, "invoice": Invoice, "provider_id": int, "info": PaymentRequestedInfo, "shipping": ShippingOption, "currency": "string", "total_amount": long, "credentials_title": "string", "users": [User]}
```


Or, if you're into Lua:

```lua
payments_paymentReceipt={_='payments.paymentReceipt', date=int, bot_id=int, invoice=Invoice, provider_id=int, info=PaymentRequestedInfo, shipping=ShippingOption, currency='string', total_amount=long, credentials_title='string', users={User}}

```


