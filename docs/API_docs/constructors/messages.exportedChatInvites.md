---
title: "messages.exportedChatInvites"
description: "messages.exportedChatInvites attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_exportedChatInvites.html
---
# Constructor: messages.exportedChatInvites  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|invites|Array of [ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.ExportedChatInvites](/API_docs/types/messages.ExportedChatInvites.html)


### Example:

```php
$messages_exportedChatInvites = ['_' => 'messages.exportedChatInvites', 'count' => int, 'invites' => [ExportedChatInvite, ExportedChatInvite], 'users' => [User, User]];
```  
