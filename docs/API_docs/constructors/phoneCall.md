---
title: "phoneCall"
description: "Phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCall  
[Back to constructors index](index.md)



Phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|p2p\_allowed|[Bool](../types/Bool.md) | Optional|Whether P2P connection to the other peer is allowed|
|video|[Bool](../types/Bool.md) | Optional|Whether this is a video call|
|id|[long](../types/long.md) | Yes|Call ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|date|[int](../types/int.md) | Yes|Date of creation of the call|
|admin\_id|[long](../types/long.md) | Yes|
|participant\_id|[long](../types/long.md) | Yes|
|g\_a\_or\_b|[bytes](../types/bytes.md) | Yes|[Parameter for key exchange](https://core.telegram.org/api/end-to-end/voice-calls)|
|key\_fingerprint|[long](../types/long.md) | Yes|[Key fingerprint](https://core.telegram.org/api/end-to-end/voice-calls)|
|protocol|[PhoneCallProtocol](../types/PhoneCallProtocol.md) | Yes|Call protocol info to be passed to libtgvoip|
|connections|Array of [PhoneConnection](../types/PhoneConnection.md) | Yes|List of endpoints the user can connect to to exchange call data|
|start\_date|[int](../types/int.md) | Yes|When was the call actually started|



### Type: [PhoneCall](../types/PhoneCall.md)


### Example:

```php
$phoneCall = ['_' => 'phoneCall', 'p2p_allowed' => Bool, 'video' => Bool, 'id' => long, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long, 'g_a_or_b' => 'bytes', 'key_fingerprint' => long, 'protocol' => PhoneCallProtocol, 'connections' => [PhoneConnection, PhoneConnection], 'start_date' => int];
```  


Or, if you're into Lua:

```lua
phoneCall={_='phoneCall', p2p_allowed=Bool, video=Bool, id=long, access_hash=long, date=int, admin_id=long, participant_id=long, g_a_or_b='bytes', key_fingerprint=long, protocol=PhoneCallProtocol, connections={PhoneConnection}, start_date=int}

```


