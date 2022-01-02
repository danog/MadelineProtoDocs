---
title: "phoneCallRequested"
description: "Requested phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallRequested  
[Back to constructors index](index.md)



Requested phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[Bool](../types/Bool.md) | Optional|Whether this is a video call|
|id|[long](../types/long.md) | Yes|Phone call ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|date|[int](../types/int.md) | Yes|When was the phone call created|
|admin\_id|[long](../types/long.md) | Yes|
|participant\_id|[long](../types/long.md) | Yes|
|g\_a\_hash|[bytes](../types/bytes.md) | Yes|[Parameter for key exchange](https://core.telegram.org/api/end-to-end/voice-calls)|
|protocol|[PhoneCallProtocol](../types/PhoneCallProtocol.md) | Yes|Call protocol info to be passed to libtgvoip|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCallRequested = ['_' => 'phoneCallRequested', 'video' => Bool, 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long, 'g_a_hash' => 'bytes', 'protocol' => PhoneCallProtocol];
```  


Or, if you're into Lua:

```lua
phoneCallRequested={_='phoneCallRequested', video=Bool, id=long, access_hash=long, date=int, admin_id=long, participant_id=long, g_a_hash='bytes', protocol=PhoneCallProtocol}

```


