---
title: help.configSimple
description: Config simple
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.configSimple  
[Back to constructors index](index.md)



Config simple

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](../types/int.md) | Yes|Date|
|expires|[int](../types/int.md) | Yes|Expires|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|ip\_port\_list|Array of [ipPort](../constructors/ipPort.md) | Yes|Ip port list|



### Type: [help\_ConfigSimple](../types/help_ConfigSimple.md)


### Example:

```php
$help_configSimple = ['_' => 'help.configSimple', 'date' => int, 'expires' => int, 'dc_id' => int, 'ip_port_list' => [ipPort, ipPort]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.configSimple", "date": int, "expires": int, "dc_id": int, "ip_port_list": [ipPort]}
```


Or, if you're into Lua:

```lua
help_configSimple={_='help.configSimple', date=int, expires=int, dc_id=int, ip_port_list={ipPort}}

```


