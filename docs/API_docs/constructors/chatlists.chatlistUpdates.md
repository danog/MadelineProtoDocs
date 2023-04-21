---
title: "chatlists.chatlistUpdates"
description: "chatlists.chatlistUpdates attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/chatlists_chatlistUpdates.html
---
# Constructor: chatlists.chatlistUpdates  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|missing\_peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [chatlists.ChatlistUpdates](/API_docs/types/chatlists.ChatlistUpdates.html)


### Example:

```
$chatlists_chatlistUpdates = ['_' => 'chatlists.chatlistUpdates', 'missing_peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
