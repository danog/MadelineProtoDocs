---
title: "messages.peerSettings"
description: "Peer settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_peerSettings.html
---
# Constructor: messages.peerSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Peer settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|settings|[PeerSettings](/API_docs/types/PeerSettings.html) | Yes|Peer settings|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [messages.PeerSettings](/API_docs/types/messages.PeerSettings.html)


### Example:

```
$messages_peerSettings = ['_' => 'messages.peerSettings', 'settings' => PeerSettings, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
