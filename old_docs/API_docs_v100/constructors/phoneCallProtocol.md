---
title: phoneCallProtocol
description: Phone call protocol
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallProtocol  
[Back to constructors index](index.md)



Phone call protocol

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|udp\_p2p|[Bool](../types/Bool.md) | Optional|Udp p2p?|
|udp\_reflector|[Bool](../types/Bool.md) | Optional|Udp reflector?|
|min\_layer|[int](../types/int.md) | Yes|Min layer|
|max\_layer|[int](../types/int.md) | Yes|Max layer|



### Type: [PhoneCallProtocol](../types/PhoneCallProtocol.md)


### Example:

```php
$phoneCallProtocol = ['_' => 'phoneCallProtocol', 'udp_p2p' => Bool, 'udp_reflector' => Bool, 'min_layer' => int, 'max_layer' => int];
```  


Or, if you're into Lua:

```lua
phoneCallProtocol={_='phoneCallProtocol', udp_p2p=Bool, udp_reflector=Bool, min_layer=int, max_layer=int}

```


