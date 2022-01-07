---
title: "messages.dialogsSlice"
description: "Incomplete list of dialogs with messages and auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_dialogsSlice.html
---
# Constructor: messages.dialogsSlice  
[Back to constructors index](/API_docs/constructors/index.md)



Incomplete list of dialogs with messages and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.md) | Yes|Total number of dialogs|
|dialogs|Array of [Dialog](/API_docs/types/Dialog.md) | Yes|List of dialogs|
|messages|Array of [Message](/API_docs/types/Message.md) | Yes|List of last messages from dialogs|
|chats|Array of [Chat](/API_docs/types/Chat.md) | Yes|List of chats mentioned in dialogs|
|users|Array of [User](/API_docs/types/User.md) | Yes|List of users mentioned in messages and chats|



### Type: [messages.Dialogs](/API_docs/types/messages.Dialogs.md)


### Example:

```php
$messages_dialogsSlice = ['_' => 'messages.dialogsSlice', 'count' => int, 'dialogs' => [Dialog, Dialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
