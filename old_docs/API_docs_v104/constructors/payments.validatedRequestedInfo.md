---
title: payments.validatedRequestedInfo
description: Validated user-provided info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: payments.validatedRequestedInfo  
[Back to constructors index](index.md)



Validated user-provided info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Optional|ID|
|shipping\_options|Array of [ShippingOption](../types/ShippingOption.md) | Optional|Shipping options|



### Type: [payments.ValidatedRequestedInfo](../types/payments.ValidatedRequestedInfo.md)


### Example:

```php
$payments.validatedRequestedInfo = ['_' => 'payments.validatedRequestedInfo', 'id' => 'string', 'shipping_options' => [ShippingOption, ShippingOption]];
```  


Or, if you're into Lua:

```lua
payments.validatedRequestedInfo={_='payments.validatedRequestedInfo', id='string', shipping_options={ShippingOption}}

```


