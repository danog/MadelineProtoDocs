---
title: "messages.exportedChatInviteReplaced"
description: "The specified chat invite was replaced with another one"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_exportedChatInviteReplaced.html
---
# Constructor: messages.exportedChatInviteReplaced  
[Back to constructors index](/API_docs/constructors/index.html)



The specified chat invite was replaced with another one

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|The replaced chat invite|
|new\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|The invite that replaces the previous invite|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.html)


### Example:

```
$messages_exportedChatInviteReplaced = ['_' => 'messages.exportedChatInviteReplaced', 'invite' => ExportedChatInvite, 'new_invite' => ExportedChatInvite, 'users' => [User, User]];
```  
