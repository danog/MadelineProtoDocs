---
title: payments.paymentVerficationNeeded
description: Payment verfication needed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_paymentVerficationNeeded.html
---
# Constructor: payments.paymentVerficationNeeded  
[Back to constructors index](index.md)



Payment verfication needed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|



### Type: [payments.PaymentResult](../types/payments.PaymentResult.md)


### Example:

```php
$payments.paymentVerficationNeeded = ['_' => 'payments.paymentVerficationNeeded', 'url' => 'string'];
```  


Or, if you're into Lua:

```lua
payments.paymentVerficationNeeded={_='payments.paymentVerficationNeeded', url='string'}

```


