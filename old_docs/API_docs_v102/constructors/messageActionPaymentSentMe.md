---
title: messageActionPaymentSentMe
description: Message action payment sent me
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaymentSentMe  
[Back to constructors index](index.md)



Message action payment sent me

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|currency|[string](../types/string.md) | Yes|Currency|
|total\_amount|[long](../types/long.md) | Yes|Total amount|
|payload|[bytes](../types/bytes.md) | Yes|Payload|
|info|[PaymentRequestedInfo](../types/PaymentRequestedInfo.md) | Optional|Info|
|shipping\_option\_id|[string](../types/string.md) | Optional|Shipping option ID|
|charge|[PaymentCharge](../types/PaymentCharge.md) | Yes|Charge|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionPaymentSentMe = ['_' => 'messageActionPaymentSentMe', 'currency' => 'string', 'total_amount' => long, 'payload' => 'bytes', 'info' => PaymentRequestedInfo, 'shipping_option_id' => 'string', 'charge' => PaymentCharge];
```  


Or, if you're into Lua:

```lua
messageActionPaymentSentMe={_='messageActionPaymentSentMe', currency='string', total_amount=long, payload='bytes', info=PaymentRequestedInfo, shipping_option_id='string', charge=PaymentCharge}

```


