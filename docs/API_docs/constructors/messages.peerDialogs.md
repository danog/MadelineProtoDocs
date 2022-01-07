---
title: "messages.peerDialogs"
description: "Dialog info of multiple peers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_peerDialogs.html
---
# Constructor: messages.peerDialogs  
[Back to constructors index](index.md)



Dialog info of multiple peers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dialogs|Array of [Dialog](../types/Dialog.md) | Yes|Dialog info|
|messages|Array of [Message](../types/Message.md) | Yes|Messages mentioned in dialog info|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|
|state|[updates.State](../constructors/updates.State.md) | Yes|Current [update state of dialog](https://core.telegram.org/api/updates)|



### Type: [messages.PeerDialogs](../types/messages.PeerDialogs.md)


### Example:

```php
$messages_peerDialogs = ['_' => 'messages.peerDialogs', 'dialogs' => [Dialog, Dialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User], 'state' => updates.State];
```  
