---
title: "messages.exportedChatInvites"
description: "messages.exportedChatInvites attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_exportedChatInvites.html
---
# Constructor: messages.exportedChatInvites  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.md) | Yes|
|invites|Array of [ExportedChatInvite](/API_docs/types/ExportedChatInvite.md) | Yes|
|users|Array of [User](/API_docs/types/User.md) | Yes|



### Type: [messages.ExportedChatInvites](/API_docs/types/messages.ExportedChatInvites.md)


### Example:

```php
$messages_exportedChatInvites = ['_' => 'messages.exportedChatInvites', 'count' => int, 'invites' => [ExportedChatInvite, ExportedChatInvite], 'users' => [User, User]];
```  
