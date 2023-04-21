---
title: "chatlists.chatlistInviteAlready"
description: "chatlists.chatlistInviteAlready attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/chatlists_chatlistInviteAlready.html
---
# Constructor: chatlists.chatlistInviteAlready  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|filter\_id|[int](/API_docs/types/int.html) | Yes|
|missing\_peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|
|already\_peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [chatlists.ChatlistInvite](/API_docs/types/chatlists.ChatlistInvite.html)


### Example:

```
$chatlists_chatlistInviteAlready = ['_' => 'chatlists.chatlistInviteAlready', 'filter_id' => int, 'missing_peers' => [Peer, Peer], 'already_peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
