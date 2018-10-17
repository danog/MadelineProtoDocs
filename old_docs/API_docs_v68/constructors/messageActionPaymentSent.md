---
title: messageActionPaymentSent
description: messageActionPaymentSent attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaymentSent  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|currency|[string](../types/string.md) | Yes|
|total\_amount|[long](../types/long.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionPaymentSent = ['_' => 'messageActionPaymentSent', 'currency' => 'string', 'total_amount' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionPaymentSent", "currency": "string", "total_amount": long}
```


Or, if you're into Lua:

```lua
messageActionPaymentSent={_='messageActionPaymentSent', currency='string', total_amount=long}

```


