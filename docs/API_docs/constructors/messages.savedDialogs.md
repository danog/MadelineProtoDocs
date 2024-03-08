---
title: "messages.savedDialogs"
description: "Represents some saved message dialogs »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_savedDialogs.html
---
# Constructor: messages.savedDialogs  
[Back to constructors index](/API_docs/constructors/index.html)



Represents some [saved message dialogs »](https://core.telegram.org/api/saved-messages).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dialogs|Array of [SavedDialog](/API_docs/types/SavedDialog.html) | Yes|[Saved message dialogs »](https://core.telegram.org/api/saved-messages).|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|List of last messages from each saved dialog|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [messages.SavedDialogs](/API_docs/types/messages.SavedDialogs.html)


### Example:

```
$messages_savedDialogs = ['_' => 'messages.savedDialogs', 'dialogs' => [SavedDialog, SavedDialog], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
