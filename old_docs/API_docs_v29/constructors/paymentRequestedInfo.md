---
title: paymentRequestedInfo
description: Order info provided by the user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: paymentRequestedInfo  
[Back to constructors index](index.md)



Order info provided by the user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](../types/string.md) | Optional|User's full name|
|phone|[string](../types/string.md) | Optional|User's phone number|
|email|[string](../types/string.md) | Optional|User's email address|
|shipping\_address|[PostAddress](../types/PostAddress.md) | Optional|User's shipping address|



### Type: [PaymentRequestedInfo](../types/PaymentRequestedInfo.md)


### Example:

```php
$paymentRequestedInfo = ['_' => 'paymentRequestedInfo', 'name' => 'string', 'phone' => 'string', 'email' => 'string', 'shipping_address' => PostAddress];
```  


Or, if you're into Lua:

```lua
paymentRequestedInfo={_='paymentRequestedInfo', name='string', phone='string', email='string', shipping_address=PostAddress}

```


