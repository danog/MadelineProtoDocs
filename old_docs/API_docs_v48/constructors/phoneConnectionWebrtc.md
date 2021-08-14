---
title: phoneConnectionWebrtc
description: WebRTC connection parameters
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneConnectionWebrtc  
[Back to constructors index](index.md)



WebRTC connection parameters

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|turn|[Bool](../types/Bool.md) | Optional|Whether this is a TURN endpoint|
|stun|[Bool](../types/Bool.md) | Optional|Whether this is a STUN endpoint|
|id|[long](../types/long.md) | Yes|Endpoint ID|
|ip|[string](../types/string.md) | Yes|IP address|
|ipv6|[string](../types/string.md) | Yes|IPv6 address|
|port|[int](../types/int.md) | Yes|Port|
|username|[string](../types/string.md) | Yes|Username|
|password|[string](../types/string.md) | Yes|Password|



### Type: [PhoneConnection](../types/PhoneConnection.md)


### Example:

```php
$phoneConnectionWebrtc = ['_' => 'phoneConnectionWebrtc', 'turn' => Bool, 'stun' => Bool, 'id' => long, 'ip' => 'string', 'ipv6' => 'string', 'port' => int, 'username' => 'string', 'password' => 'string'];
```  


Or, if you're into Lua:

```lua
phoneConnectionWebrtc={_='phoneConnectionWebrtc', turn=Bool, stun=Bool, id=long, ip='string', ipv6='string', port=int, username='string', password='string'}

```


