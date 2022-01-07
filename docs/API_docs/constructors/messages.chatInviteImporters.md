---
title: "messages.chatInviteImporters"
description: "messages.chatInviteImporters attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatInviteImporters.html
---
# Constructor: messages.chatInviteImporters  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|importers|Array of [ChatInviteImporter](/API_docs/types/ChatInviteImporter.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.ChatInviteImporters](/API_docs/types/messages.ChatInviteImporters.html)


### Example:

```php
$messages_chatInviteImporters = ['_' => 'messages.chatInviteImporters', 'count' => int, 'importers' => [ChatInviteImporter, ChatInviteImporter], 'users' => [User, User]];
```  
