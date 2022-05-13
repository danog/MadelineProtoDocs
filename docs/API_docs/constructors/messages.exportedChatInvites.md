---
title: "messages.exportedChatInvites"
description: "Info about chat invites exported by a certain admin."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_exportedChatInvites.html
---
# Constructor: messages.exportedChatInvites  
[Back to constructors index](/API_docs/constructors/index.html)



Info about chat invites exported by a certain admin.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Number of invites exported by the admin|
|invites|Array of [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|Exported invites|
|users|Array of [User](/API_docs/types/User.html) | Yes|Info about the admin|



### Type: [messages.ExportedChatInvites](/API_docs/types/messages.ExportedChatInvites.html)


### Example:

```
$messages_exportedChatInvites = ['_' => 'messages.exportedChatInvites', 'count' => int, 'invites' => [ExportedChatInvite, ExportedChatInvite], 'users' => [User, User]];
```  
