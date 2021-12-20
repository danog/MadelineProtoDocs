---
title: "phoneConnection"
description: "Identifies an endpoint that can be used to connect to the other user in a phone call"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneConnection  
[Back to constructors index](index.md)



Identifies an endpoint that can be used to connect to the other user in a phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Endpoint ID|
|ip|[string](../types/string.md) | Yes|IP address of endpoint|
|ipv6|[string](../types/string.md) | Yes|IPv6 address of endpoint|
|port|[int](../types/int.md) | Yes|Port ID|
|peer\_tag|[bytes](../types/bytes.md) | Yes|Our peer tag|



### Type: [PhoneConnection](../types/PhoneConnection.md)


### Example:

```php
$phoneConnection = ['_' => 'phoneConnection', 'id' => long, 'ip' => 'string', 'ipv6' => 'string', 'port' => int, 'peer_tag' => 'bytes'];
```  


Or, if you're into Lua:

```lua
phoneConnection={_='phoneConnection', id=long, ip='string', ipv6='string', port=int, peer_tag='bytes'}

```


