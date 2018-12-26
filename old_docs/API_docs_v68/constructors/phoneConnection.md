---
title: phoneConnection
description: Phone connection
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneConnection  
[Back to constructors index](index.md)



Phone connection

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|ip|[string](../types/string.md) | Yes|Ip|
|ipv6|[string](../types/string.md) | Yes|Ipv6|
|port|[int](../types/int.md) | Yes|Port|
|peer\_tag|[bytes](../types/bytes.md) | Yes|Peer tag|



### Type: [PhoneConnection](../types/PhoneConnection.md)


### Example:

```php
$phoneConnection = ['_' => 'phoneConnection', 'id' => long, 'ip' => 'string', 'ipv6' => 'string', 'port' => int, 'peer_tag' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "phoneConnection", "id": long, "ip": "string", "ipv6": "string", "port": int, "peer_tag": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
phoneConnection={_='phoneConnection', id=long, ip='string', ipv6='string', port=int, peer_tag='bytes'}

```


