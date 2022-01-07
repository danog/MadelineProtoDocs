---
title: "messages.peerSettings"
description: "messages.peerSettings attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_peerSettings.html
---
# Constructor: messages.peerSettings  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|settings|[PeerSettings](/API_docs/types/PeerSettings.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.PeerSettings](/API_docs/types/messages.PeerSettings.html)


### Example:

```php
$messages_peerSettings = ['_' => 'messages.peerSettings', 'settings' => PeerSettings, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
