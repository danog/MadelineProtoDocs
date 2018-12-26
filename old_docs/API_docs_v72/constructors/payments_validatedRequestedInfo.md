---
title: payments.validatedRequestedInfo
description: Validated requested info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: payments.validatedRequestedInfo  
[Back to constructors index](index.md)



Validated requested info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Optional|ID|
|shipping\_options|Array of [ShippingOption](../types/ShippingOption.md) | Optional|Shipping options|



### Type: [payments\_ValidatedRequestedInfo](../types/payments_ValidatedRequestedInfo.md)


### Example:

```php
$payments_validatedRequestedInfo = ['_' => 'payments.validatedRequestedInfo', 'id' => 'string', 'shipping_options' => [ShippingOption, ShippingOption]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "payments.validatedRequestedInfo", "id": "string", "shipping_options": [ShippingOption]}
```


Or, if you're into Lua:

```lua
payments_validatedRequestedInfo={_='payments.validatedRequestedInfo', id='string', shipping_options={ShippingOption}}

```


