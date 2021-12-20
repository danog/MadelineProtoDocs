---
title: "paymentCharge"
description: "Payment identifier"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: paymentCharge  
[Back to constructors index](index.md)



Payment identifier

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|Telegram payment identifier|
|provider\_charge\_id|[string](../types/string.md) | Yes|Provider payment identifier|



### Type: [PaymentCharge](../types/PaymentCharge.md)


### Example:

```php
$paymentCharge = ['_' => 'paymentCharge', 'id' => 'string', 'provider_charge_id' => 'string'];
```  


Or, if you're into Lua:

```lua
paymentCharge={_='paymentCharge', id='string', provider_charge_id='string'}

```


