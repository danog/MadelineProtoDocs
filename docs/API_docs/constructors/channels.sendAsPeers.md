---
title: "channels.sendAsPeers"
description: "channels.sendAsPeers attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_sendAsPeers.html
---
# Constructor: channels.sendAsPeers  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peers|Array of [Peer](/API_docs/types/Peer.md) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.md) | Yes|
|users|Array of [User](/API_docs/types/User.md) | Yes|



### Type: [channels.SendAsPeers](/API_docs/types/channels.SendAsPeers.md)


### Example:

```php
$channels_sendAsPeers = ['_' => 'channels.sendAsPeers', 'peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
