---
title: help.proxyDataPromo
description: Promotion channel associated to a certain MTProxy
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.proxyDataPromo  
[Back to constructors index](index.md)



Promotion channel associated to a certain MTProxy

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|Expiration date of proxy info, will have to be refetched in `expires` seconds|
|peer|[Peer](../types/Peer.md) | Yes|The promoted channel|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [help\_ProxyData](../types/help_ProxyData.md)


### Example:

```php
$help_proxyDataPromo = ['_' => 'help.proxyDataPromo', 'expires' => int, 'peer' => Peer, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
help_proxyDataPromo={_='help.proxyDataPromo', expires=int, peer=Peer, chats={Chat}, users={User}}

```


