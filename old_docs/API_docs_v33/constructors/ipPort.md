---
title: ipPort
description: ipPort attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: ipPort  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|ipv4|[int](../types/int.md) | Yes|
|port|[int](../types/int.md) | Yes|



### Type: [IpPort](../types/IpPort.md)


### Example:

```php
$ipPort = ['_' => 'ipPort', 'ipv4' => int, 'port' => int];
```  


Or, if you're into Lua:

```lua
ipPort={_='ipPort', ipv4=int, port=int}

```


