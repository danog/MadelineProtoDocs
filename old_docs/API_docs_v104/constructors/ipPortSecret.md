---
title: ipPortSecret
description: Ip port secret
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: ipPortSecret  
[Back to constructors index](index.md)



Ip port secret

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ipv4|[int](../types/int.md) | Yes|Ipv4|
|port|[int](../types/int.md) | Yes|Port|
|secret|[bytes](../types/bytes.md) | Yes|Secret|



### Type: [IpPort](../types/IpPort.md)


### Example:

```php
$ipPortSecret = ['_' => 'ipPortSecret', 'ipv4' => int, 'port' => int, 'secret' => 'bytes'];
```  


Or, if you're into Lua:

```lua
ipPortSecret={_='ipPortSecret', ipv4=int, port=int, secret='bytes'}

```


