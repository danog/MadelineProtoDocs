---
title: "messages.dialogs"
description: "Full list of chats with messages and auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dialogs.html
---
# Constructor: messages.dialogs  
[Back to constructors index](/API_docs/constructors/index.html)



Full list of chats with messages and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dialogs|Array of [Dialog](/API_docs/types/Dialog.html) | Yes|List of chats|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|List of last messages from each chat|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|List of groups mentioned in the chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of users mentioned in messages and groups|



### Type: [messages.Dialogs](/API_docs/types/messages.Dialogs.html)


### Example:

```
$messages_dialogs = ['_' => 'messages.dialogs', 'dialogs' => [Dialog, Dialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
