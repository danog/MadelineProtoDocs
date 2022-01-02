---
title: "phoneCallProtocol"
description: "Protocol info for libtgvoip"
nav_exclude: true
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
|library\_versions|Array of [string](../types/string.md) | Yes|When using [phone.requestCall](../methods/phone.requestCall.md) and [phone.acceptCall](../methods/phone.acceptCall.md), specify all library versions supported by the client. <br>The server will merge and choose the best library version supported by both peers, returning only the best value in the result of the callee's [phone.acceptCall](../methods/phone.acceptCall.md) and in the [phoneCallAccepted](../constructors/phoneCallAccepted.md) update received by the caller.|



### Type: [PhoneCallProtocol](../types/PhoneCallProtocol.md)


### Example:

```php
$phoneCallProtocol = ['_' => 'phoneCallProtocol', 'udp_p2p' => Bool, 'udp_reflector' => Bool, 'min_layer' => int, 'max_layer' => int, 'library_versions' => ['string', 'string']];
```  


Or, if you're into Lua:

```lua
phoneCallProtocol={_='phoneCallProtocol', udp_p2p=Bool, udp_reflector=Bool, min_layer=int, max_layer=int, library_versions={'string'}}

```


