---
title: phoneConnection
description: phoneConnection attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneConnection  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|ip|[string](../types/string.md) | Yes|
|ipv6|[string](../types/string.md) | Yes|
|port|[int](../types/int.md) | Yes|
|peer\_tag|[bytes](../types/bytes.md) | Yes|



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


