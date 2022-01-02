---
title: "phoneCallAccepted"
description: "An accepted phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallAccepted  
[Back to constructors index](index.md)



An accepted phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[Bool](../types/Bool.md) | Optional|Whether this is a video call|
|id|[long](../types/long.md) | Yes|ID of accepted phone call|
|access\_hash|[long](../types/long.md) | Yes|Access hash of phone call|
|date|[int](../types/int.md) | Yes|When was the call accepted|
|admin\_id|[long](../types/long.md) | Yes|
|participant\_id|[long](../types/long.md) | Yes|
|g\_b|[bytes](../types/bytes.md) | Yes|B parameter for [secure E2E phone call key exchange](https://core.telegram.org/api/end-to-end/voice-calls)|
|protocol|[PhoneCallProtocol](../types/PhoneCallProtocol.md) | Yes|Protocol to use for phone call|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCallAccepted = ['_' => 'phoneCallAccepted', 'video' => Bool, 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long, 'g_b' => 'bytes', 'protocol' => PhoneCallProtocol];
```  


Or, if you're into Lua:

```lua
phoneCallAccepted={_='phoneCallAccepted', video=Bool, id=long, access_hash=long, date=int, admin_id=long, participant_id=long, g_b='bytes', protocol=PhoneCallProtocol}

```


