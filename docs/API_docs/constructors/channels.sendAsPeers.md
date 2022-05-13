---
title: "channels.sendAsPeers"
description: "A list of peers that can be used to send messages in a specific group"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_sendAsPeers.html
---
# Constructor: channels.sendAsPeers  
[Back to constructors index](/API_docs/constructors/index.html)



A list of peers that can be used to send messages in a specific group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|Peers that can be used to send messages to the group|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [channels.SendAsPeers](/API_docs/types/channels.SendAsPeers.html)


### Example:

```
$channels_sendAsPeers = ['_' => 'channels.sendAsPeers', 'peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
