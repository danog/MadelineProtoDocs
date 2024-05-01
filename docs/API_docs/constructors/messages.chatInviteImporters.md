---
title: "messages.chatInviteImporters"
description: "Info about the users that joined the chat using a specific chat invite"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatInviteImporters.html
---
# Constructor: messages.chatInviteImporters  
[Back to constructors index](/API_docs/constructors/index.html)



Info about the users that joined the chat using a specific chat invite

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Number of users that joined|
|importers|Array of [ChatInviteImporter](/API_docs/types/ChatInviteImporter.html) | Yes|The users that joined|
|users|Array of [User](/API_docs/types/User.html) | Yes|The users that joined|



### Type: [messages.ChatInviteImporters](/API_docs/types/messages.ChatInviteImporters.html)


### Example:

```
$messages_chatInviteImporters = ['_' => 'messages.chatInviteImporters', 'count' => int, 'importers' => [ChatInviteImporter, ChatInviteImporter], 'users' => [User, User]];
```  
