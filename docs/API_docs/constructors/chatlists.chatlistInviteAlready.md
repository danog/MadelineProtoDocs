---
title: "chatlists.chatlistInviteAlready"
description: "Updated info about a chat folder deep link » we already imported."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/chatlists_chatlistInviteAlready.html
---
# Constructor: chatlists.chatlistInviteAlready  
[Back to constructors index](/API_docs/constructors/index.html)



Updated info about a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links) we already imported.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|filter\_id|[int](/API_docs/types/int.html) | Yes|ID of the imported folder|
|missing\_peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|New peers to be imported|
|already\_peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|Peers that were already imported|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Related chat information|
|users|Array of [User](/API_docs/types/User.html) | Yes|Related user information|



### Type: [chatlists.ChatlistInvite](/API_docs/types/chatlists.ChatlistInvite.html)


### Example:

```
$chatlists_chatlistInviteAlready = ['_' => 'chatlists.chatlistInviteAlready', 'filter_id' => int, 'missing_peers' => [Peer, Peer], 'already_peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
