---
title: help.proxyDataPromo
description: Proxy data promo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.proxyDataPromo  
[Back to constructors index](index.md)



Proxy data promo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|Expires|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [help\_ProxyData](../types/help_ProxyData.md)


### Example:

```php
$help_proxyDataPromo = ['_' => 'help.proxyDataPromo', 'expires' => int, 'peer' => Peer, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.proxyDataPromo", "expires": int, "peer": Peer, "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:

```lua
help_proxyDataPromo={_='help.proxyDataPromo', expires=int, peer=Peer, chats={Chat}, users={User}}

```


