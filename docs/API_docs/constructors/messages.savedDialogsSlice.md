---
title: "messages.savedDialogsSlice"
description: "messages.savedDialogsSlice attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_savedDialogsSlice.html
---
# Constructor: messages.savedDialogsSlice  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|dialogs|Array of [SavedDialog](/API_docs/types/SavedDialog.html) | Yes|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.SavedDialogs](/API_docs/types/messages.SavedDialogs.html)


### Example:

```
$messages_savedDialogsSlice = ['_' => 'messages.savedDialogsSlice', 'count' => int, 'dialogs' => [SavedDialog, SavedDialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
