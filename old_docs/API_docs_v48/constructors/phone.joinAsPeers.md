---
title: phone.joinAsPeers
description: phone.joinAsPeers attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_joinAsPeers.html
---
# Constructor: phone.joinAsPeers  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peers|Array of [Peer](../types/Peer.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [phone.JoinAsPeers](../types/phone.JoinAsPeers.md)


### Example:

```php
$phone_joinAsPeers = ['_' => 'phone.joinAsPeers', 'peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
phone_joinAsPeers={_='phone.joinAsPeers', peers={Peer}, chats={Chat}, users={User}}

```


