---
title: phoneConnectionWebrtc
description: phoneConnectionWebrtc attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneConnectionWebrtc  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|turn|[Bool](../types/Bool.md) | Optional|
|stun|[Bool](../types/Bool.md) | Optional|
|id|[long](../types/long.md) | Yes|
|ip|[string](../types/string.md) | Yes|
|ipv6|[string](../types/string.md) | Yes|
|port|[int](../types/int.md) | Yes|
|username|[string](../types/string.md) | Yes|
|password|[string](../types/string.md) | Yes|



### Type: [PhoneConnection](../types/PhoneConnection.md)


### Example:

```php
$phoneConnectionWebrtc = ['_' => 'phoneConnectionWebrtc', 'turn' => Bool, 'stun' => Bool, 'id' => long, 'ip' => 'string', 'ipv6' => 'string', 'port' => int, 'username' => 'string', 'password' => 'string'];
```  


Or, if you're into Lua:

```lua
phoneConnectionWebrtc={_='phoneConnectionWebrtc', turn=Bool, stun=Bool, id=long, ip='string', ipv6='string', port=int, username='string', password='string'}

```


