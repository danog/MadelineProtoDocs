---
title: "updatePhoneCallSignalingData"
description: "Incoming phone call signaling payload"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePhoneCallSignalingData  
[Back to constructors index](index.md)



Incoming phone call signaling payload

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_call\_id|[long](../types/long.md) | Yes|Phone call ID|
|data|[bytes](../types/bytes.md) | Yes|Signaling payload|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePhoneCallSignalingData = ['_' => 'updatePhoneCallSignalingData', 'phone_call_id' => long, 'data' => 'bytes'];
```  


Or, if you're into Lua:

```lua
updatePhoneCallSignalingData={_='updatePhoneCallSignalingData', phone_call_id=long, data='bytes'}

```


