---
title: paymentRequestedInfo
description: Payment requested info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: paymentRequestedInfo  
[Back to constructors index](index.md)



Payment requested info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](../types/string.md) | Optional|Name|
|phone|[string](../types/string.md) | Optional|Phone|
|email|[string](../types/string.md) | Optional|Email|
|shipping\_address|[PostAddress](../types/PostAddress.md) | Optional|Shipping address|



### Type: [PaymentRequestedInfo](../types/PaymentRequestedInfo.md)


### Example:

```php
$paymentRequestedInfo = ['_' => 'paymentRequestedInfo', 'name' => 'string', 'phone' => 'string', 'email' => 'string', 'shipping_address' => PostAddress];
```  


Or, if you're into Lua:

```lua
paymentRequestedInfo={_='paymentRequestedInfo', name='string', phone='string', email='string', shipping_address=PostAddress}

```


