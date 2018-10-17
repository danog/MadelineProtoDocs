---
title: phoneCallRequested
description: phoneCallRequested attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallRequested  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|
|admin\_id|[int](../types/int.md) | Yes|
|participant\_id|[int](../types/int.md) | Yes|
|g\_a|[bytes](../types/bytes.md) | Yes|
|protocol|[PhoneCallProtocol](../types/PhoneCallProtocol.md) | Yes|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCallRequested = ['_' => 'phoneCallRequested', 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => int, 'participant_id' => int, 'g_a' => 'bytes', 'protocol' => PhoneCallProtocol];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "phoneCallRequested", "id": long, "access_hash": long, "date": int, "admin_id": int, "participant_id": int, "g_a": {"_": "bytes", "bytes":"base64 encoded bytes"}, "protocol": PhoneCallProtocol}
```


Or, if you're into Lua:

```lua
phoneCallRequested={_='phoneCallRequested', id=long, access_hash=long, date=int, admin_id=int, participant_id=int, g_a='bytes', protocol=PhoneCallProtocol}

```


