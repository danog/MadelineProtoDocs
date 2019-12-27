---
title: payments.paymentVerificationNeeded
description: Payment was not successful, additional verification is needed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: payments.paymentVerificationNeeded  
[Back to constructors index](index.md)



Payment was not successful, additional verification is needed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL for additional payment credentials verification|



### Type: [payments.PaymentResult](../types/payments.PaymentResult.md)


### Example:

```php
$payments.paymentVerificationNeeded = ['_' => 'payments.paymentVerificationNeeded', 'url' => 'string'];
```  


Or, if you're into Lua:

```lua
payments.paymentVerificationNeeded={_='payments.paymentVerificationNeeded', url='string'}

```


