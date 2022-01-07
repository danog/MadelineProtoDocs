---
title: "phone.joinAsPeers"
description: "phone.joinAsPeers attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_joinAsPeers.html
---
# Constructor: phone.joinAsPeers  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [phone.JoinAsPeers](/API_docs/types/phone.JoinAsPeers.html)


### Example:

```php
$phone_joinAsPeers = ['_' => 'phone.joinAsPeers', 'peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
