---
title: "messages.exportedChatInvite"
description: "Info about a chat invite"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_exportedChatInvite.html
---
# Constructor: messages.exportedChatInvite  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a chat invite

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|Info about the chat invite|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.html)


### Example:

```
$messages_exportedChatInvite = ['_' => 'messages.exportedChatInvite', 'invite' => ExportedChatInvite, 'users' => [User, User]];
```  
