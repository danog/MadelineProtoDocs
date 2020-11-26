---
title: updatePhoneCallSignalingData
description: updatePhoneCallSignalingData attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePhoneCallSignalingData  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|phone\_call\_id|[long](../types/long.md) | Yes|
|data|[bytes](../types/bytes.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePhoneCallSignalingData = ['_' => 'updatePhoneCallSignalingData', 'phone_call_id' => long, 'data' => 'bytes'];
```  


Or, if you're into Lua:

```lua
updatePhoneCallSignalingData={_='updatePhoneCallSignalingData', phone_call_id=long, data='bytes'}

```


