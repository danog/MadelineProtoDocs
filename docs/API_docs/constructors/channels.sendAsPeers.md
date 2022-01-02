---
title: "channels.sendAsPeers"
description: "channels.sendAsPeers attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_sendAsPeers.html
---
# Constructor: channels.sendAsPeers  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peers|Array of [Peer](../types/Peer.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [channels.SendAsPeers](../types/channels.SendAsPeers.md)


### Example:

```php
$channels_sendAsPeers = ['_' => 'channels.sendAsPeers', 'peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
channels_sendAsPeers={_='channels.sendAsPeers', peers={Peer}, chats={Chat}, users={User}}

```


