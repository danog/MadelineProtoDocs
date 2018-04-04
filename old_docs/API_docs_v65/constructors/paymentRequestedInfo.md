---
title: paymentRequestedInfo
description: paymentRequestedInfo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: paymentRequestedInfo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|name|[string](../types/string.md) | Optional|
|phone|[string](../types/string.md) | Optional|
|email|[string](../types/string.md) | Optional|
|shipping\_address|[PostAddress](../types/PostAddress.md) | Optional|



### Type: [PaymentRequestedInfo](../types/PaymentRequestedInfo.md)


### Example:

```
$paymentRequestedInfo = ['_' => 'paymentRequestedInfo', 'name' => 'string', 'phone' => 'string', 'email' => 'string', 'shipping_address' => PostAddress];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "paymentRequestedInfo", "name": "string", "phone": "string", "email": "string", "shipping_address": PostAddress}
```


Or, if you're into Lua:  


```
paymentRequestedInfo={_='paymentRequestedInfo', name='string', phone='string', email='string', shipping_address=PostAddress}

```


