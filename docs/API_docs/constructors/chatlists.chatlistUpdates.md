---
title: "chatlists.chatlistUpdates"
description: "Updated information about a chat folder deep link »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/chatlists_chatlistUpdates.html
---
# Constructor: chatlists.chatlistUpdates  
[Back to constructors index](/API_docs/constructors/index.html)



Updated information about a [chat folder deep link »](https://core.telegram.org/api/links#chat-folder-links).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|missing\_peers|Array of [Peer](/API_docs/types/Peer.html) | Yes|New peers to join|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Related chat information|
|users|Array of [User](/API_docs/types/User.html) | Yes|Related user information|



### Type: [chatlists.ChatlistUpdates](/API_docs/types/chatlists.ChatlistUpdates.html)


### Example:

```
$chatlists_chatlistUpdates = ['_' => 'chatlists.chatlistUpdates', 'missing_peers' => [Peer, Peer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
