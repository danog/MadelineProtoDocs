---
title: updateBotPrecheckoutQuery
description: This object contains information about an incoming pre-checkout query.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotPrecheckoutQuery  
[Back to constructors index](index.md)



This object contains information about an incoming pre-checkout query.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Unique query identifier|
|user\_id|[int](../types/int.md) | Yes|User who sent the query|
|payload|[bytes](../types/bytes.md) | Yes|Bot specified invoice payload|
|info|[PaymentRequestedInfo](../types/PaymentRequestedInfo.md) | Optional|Order info provided by the user|
|shipping\_option\_id|[string](../types/string.md) | Optional|Identifier of the shipping option chosen by the user|
|currency|[string](../types/string.md) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](../types/long.md) | Yes|Total amount in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotPrecheckoutQuery = ['_' => 'updateBotPrecheckoutQuery', 'query_id' => long, 'user_id' => int, 'payload' => 'bytes', 'info' => PaymentRequestedInfo, 'shipping_option_id' => 'string', 'currency' => 'string', 'total_amount' => long];
```  


Or, if you're into Lua:

```lua
updateBotPrecheckoutQuery={_='updateBotPrecheckoutQuery', query_id=long, user_id=int, payload='bytes', info=PaymentRequestedInfo, shipping_option_id='string', currency='string', total_amount=long}

```


