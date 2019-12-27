---
title: payments.paymentResult
description: Payment result
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: payments.paymentResult  
[Back to constructors index](index.md)



Payment result

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|updates|[Updates](../types/Updates.md) | Yes|Info about the payment|



### Type: [payments.PaymentResult](../types/payments.PaymentResult.md)


### Example:

```php
$payments.paymentResult = ['_' => 'payments.paymentResult', 'updates' => Updates];
```  


Or, if you're into Lua:

```lua
payments.paymentResult={_='payments.paymentResult', updates=Updates}

```


