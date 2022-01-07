---
title: "messages.exportedChatInviteReplaced"
description: "messages.exportedChatInviteReplaced attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_exportedChatInviteReplaced.html
---
# Constructor: messages.exportedChatInviteReplaced  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.md) | Yes|
|new\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.md) | Yes|
|users|Array of [User](/API_docs/types/User.md) | Yes|



### Type: [messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.md)


### Example:

```php
$messages_exportedChatInviteReplaced = ['_' => 'messages.exportedChatInviteReplaced', 'invite' => ExportedChatInvite, 'new_invite' => ExportedChatInvite, 'users' => [User, User]];
```  
