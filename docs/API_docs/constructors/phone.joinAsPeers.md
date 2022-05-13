---
title: "phone.joinAsPeers"
description: "A list of peers that can be used to join a group call, presenting yourself as a specific user/channel."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_joinAsPeers.html
---
# Constructor: phone.joinAsPeers  
[Back to constructors index](/API_docs/constructors/index.html)



A list of peers that can be used to join a group call, presenting yourself as a specific user/channel.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|Peers|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats mentioned in the peers vector|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the peers vector|



### Type: [phone.JoinAsPeers](/API_docs/types/phone.JoinAsPeers.html)


### Example:

```
$phone_joinAsPeers = ['_' => 'phone.joinAsPeers', 'peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
