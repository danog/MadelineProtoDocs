---
title: "messages.inactiveChats"
description: "Inactive chat list"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_inactiveChats.html
---
# Constructor: messages.inactiveChats  
[Back to constructors index](/API_docs/constructors/index.html)



Inactive chat list

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dates|Array of [int](/API_docs/types/int.html) | Yes|When was the chat last active|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chat list|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in the chat list|



### Type: [messages.InactiveChats](/API_docs/types/messages.InactiveChats.html)


### Example:

```
$messages_inactiveChats = ['_' => 'messages.inactiveChats', 'dates' => [int, int], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
