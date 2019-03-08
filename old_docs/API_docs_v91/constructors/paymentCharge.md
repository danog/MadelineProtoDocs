---
title: paymentCharge
description: Payment charge
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: paymentCharge  
[Back to constructors index](index.md)



Payment charge

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|ID|
|provider\_charge\_id|[string](../types/string.md) | Yes|Provider charge ID|



### Type: [PaymentCharge](../types/PaymentCharge.md)


### Example:

```php
$paymentCharge = ['_' => 'paymentCharge', 'id' => 'string', 'provider_charge_id' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "paymentCharge", "id": "string", "provider_charge_id": "string"}
```


Or, if you're into Lua:

```lua
paymentCharge={_='paymentCharge', id='string', provider_charge_id='string'}

```


