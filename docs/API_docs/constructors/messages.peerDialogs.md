---
title: "messages.peerDialogs"
description: "Dialog info of multiple peers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_peerDialogs.html
---
# Constructor: messages.peerDialogs  
[Back to constructors index](/API_docs/constructors/index.html)



Dialog info of multiple peers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dialogs|Array of [Dialog](/API_docs/types/Dialog.html) | Yes|Dialog info|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|Messages mentioned in dialog info|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|
|state|[updates.State](/API_docs/constructors/updates.State.html) | Yes|Current [update state of dialog](https://core.telegram.org/api/updates)|



### Type: [messages.PeerDialogs](/API_docs/types/messages.PeerDialogs.html)


### Example:

```
$messages_peerDialogs = ['_' => 'messages.peerDialogs', 'dialogs' => [Dialog, Dialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User], 'state' => updates.State];
```  
