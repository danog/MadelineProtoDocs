---
title: phoneCallProtocol
description: Protocol info for libtgvoip
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallProtocol  
[Back to constructors index](index.md)



Protocol info for libtgvoip

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|udp\_p2p|[Bool](../types/Bool.md) | Optional|Whether to allow P2P connection to the other participant|
|udp\_reflector|[Bool](../types/Bool.md) | Optional|Whether to allow connection to the other participants through the reflector servers|
|min\_layer|[int](../types/int.md) | Yes|Minimum layer for remote libtgvoip|
|max\_layer|[int](../types/int.md) | Yes|Maximum layer for remote libtgvoip|



### Type: [PhoneCallProtocol](../types/PhoneCallProtocol.md)


### Example:

```php
$phoneCallProtocol = ['_' => 'phoneCallProtocol', 'udp_p2p' => Bool, 'udp_reflector' => Bool, 'min_layer' => int, 'max_layer' => int];
```  


Or, if you're into Lua:

```lua
phoneCallProtocol={_='phoneCallProtocol', udp_p2p=Bool, udp_reflector=Bool, min_layer=int, max_layer=int}

```


