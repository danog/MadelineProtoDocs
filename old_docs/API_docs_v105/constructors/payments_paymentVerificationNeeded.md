---
title: payments.paymentVerificationNeeded
description: Payment verification needed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: payments.paymentVerificationNeeded  
[Back to constructors index](index.md)



Payment verification needed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|3dsecure URL|



### Type: [payments\_PaymentResult](../types/payments_PaymentResult.md)


### Example:

```php
$payments_paymentVerificationNeeded = ['_' => 'payments.paymentVerificationNeeded', 'url' => 'string'];
```  


Or, if you're into Lua:

```lua
payments_paymentVerificationNeeded={_='payments.paymentVerificationNeeded', url='string'}

```


