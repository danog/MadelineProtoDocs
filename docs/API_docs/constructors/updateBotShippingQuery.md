---
title: "updateBotShippingQuery"
description: "This object contains information about an incoming shipping query."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotShippingQuery  
[Back to constructors index](index.md)



This object contains information about an incoming shipping query.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|query\_id|[long](../types/long.md) | Yes|Unique query identifier|
|user\_id|[long](../types/long.md) | Yes|
|payload|[bytes](../types/bytes.md) | Yes|Bot specified invoice payload|
|shipping\_address|[PostAddress](../types/PostAddress.md) | Yes|User specified shipping address|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateBotShippingQuery = ['_' => 'updateBotShippingQuery', 'query_id' => long, 'user_id' => long, 'payload' => 'bytes', 'shipping_address' => PostAddress];
```  
