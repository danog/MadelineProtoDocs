---
title: "messages.savedDialogsSlice"
description: "Incomplete list of saved message dialogs » with messages and auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_savedDialogsSlice.html
---
# Constructor: messages.savedDialogsSlice  
[Back to constructors index](/API_docs/constructors/index.html)



Incomplete list of [saved message dialogs »](https://core.telegram.org/api/saved-messages) with messages and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of saved message dialogs|
|dialogs|Array of [SavedDialog](/API_docs/types/SavedDialog.html) | Yes|List of saved message dialogs|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|List of last messages from dialogs|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [messages.SavedDialogs](/API_docs/types/messages.SavedDialogs.html)


### Example:

```
$messages_savedDialogsSlice = ['_' => 'messages.savedDialogsSlice', 'count' => int, 'dialogs' => [SavedDialog, SavedDialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
