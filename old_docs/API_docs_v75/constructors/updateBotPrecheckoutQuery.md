---
title: updateBotPrecheckoutQuery
description: Update bot precheckout query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotPrecheckoutQuery  
[Back to constructors index](index.md)



Update bot precheckout query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|payload|[bytes](../types/bytes.md) | Yes|Payload|
|info|[PaymentRequestedInfo](../types/PaymentRequestedInfo.md) | Optional|Info|
|shipping\_option\_id|[string](../types/string.md) | Optional|Shipping option ID|
|currency|[string](../types/string.md) | Yes|Currency|
|total\_amount|[long](../types/long.md) | Yes|Total amount|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotPrecheckoutQuery = ['_' => 'updateBotPrecheckoutQuery', 'query_id' => long, 'user_id' => int, 'payload' => 'bytes', 'info' => PaymentRequestedInfo, 'shipping_option_id' => 'string', 'currency' => 'string', 'total_amount' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateBotPrecheckoutQuery", "query_id": long, "user_id": int, "payload": {"_": "bytes", "bytes":"base64 encoded bytes"}, "info": PaymentRequestedInfo, "shipping_option_id": "string", "currency": "string", "total_amount": long}
```


Or, if you're into Lua:

```lua
updateBotPrecheckoutQuery={_='updateBotPrecheckoutQuery', query_id=long, user_id=int, payload='bytes', info=PaymentRequestedInfo, shipping_option_id='string', currency='string', total_amount=long}

```


