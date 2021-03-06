---
title: ipPortSecret
description: ipPortSecret attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: ipPortSecret  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|ipv4|[int](../types/int.md) | Yes|
|port|[int](../types/int.md) | Yes|
|secret|[bytes](../types/bytes.md) | Yes|



### Type: [IpPort](../types/IpPort.md)


### Example:

```php
$ipPortSecret = ['_' => 'ipPortSecret', 'ipv4' => int, 'port' => int, 'secret' => 'bytes'];
```  


Or, if you're into Lua:

```lua
ipPortSecret={_='ipPortSecret', ipv4=int, port=int, secret='bytes'}

```


