---
title: help.proxyDataPromo
description: help_proxyDataPromo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: help.proxyDataPromo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|expires|[int](../types/int.md) | Yes|
|peer|[Peer](../types/Peer.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [help\_ProxyData](../types/help_ProxyData.md)


### Example:

```
$help_proxyDataPromo = ['_' => 'help.proxyDataPromo', 'expires' => int, 'peer' => Peer, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "help.proxyDataPromo", "expires": int, "peer": Peer, "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:  


```
help_proxyDataPromo={_='help.proxyDataPromo', expires=int, peer=Peer, chats={Chat}, users={User}}

```


