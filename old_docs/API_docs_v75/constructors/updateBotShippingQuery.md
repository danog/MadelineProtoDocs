---
title: updateBotShippingQuery
description: Update bot shipping query
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotShippingQuery  
[Back to constructors index](index.md)



Update bot shipping query

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Query ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|payload|[bytes](../types/bytes.md) | Yes|Payload|
|shipping\_address|[PostAddress](../types/PostAddress.md) | Yes|Shipping address|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotShippingQuery = ['_' => 'updateBotShippingQuery', 'query_id' => long, 'user_id' => int, 'payload' => 'bytes', 'shipping_address' => PostAddress];
```  


Or, if you're into Lua:

```lua
updateBotShippingQuery={_='updateBotShippingQuery', query_id=long, user_id=int, payload='bytes', shipping_address=PostAddress}

```


