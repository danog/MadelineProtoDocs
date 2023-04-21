---
title: "chatlists.chatlistInvite"
description: "chatlists.chatlistInvite attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/chatlists_chatlistInvite.html
---
# Constructor: chatlists.chatlistInvite  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](/API_docs/types/string.html) | Yes|
|emoticon|[string](/API_docs/types/string.html) | Optional|
|peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [chatlists.ChatlistInvite](/API_docs/types/chatlists.ChatlistInvite.html)


### Example:

```
$chatlists_chatlistInvite = ['_' => 'chatlists.chatlistInvite', 'title' => 'string', 'emoticon' => 'string', 'peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
