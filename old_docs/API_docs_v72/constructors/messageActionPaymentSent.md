---
title: messageActionPaymentSent
description: Message action payment sent
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaymentSent  
[Back to constructors index](index.md)



Message action payment sent

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|currency|[string](../types/string.md) | Yes|Currency|
|total\_amount|[long](../types/long.md) | Yes|Total amount|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionPaymentSent = ['_' => 'messageActionPaymentSent', 'currency' => 'string', 'total_amount' => long];
```  


Or, if you're into Lua:

```lua
messageActionPaymentSent={_='messageActionPaymentSent', currency='string', total_amount=long}

```


