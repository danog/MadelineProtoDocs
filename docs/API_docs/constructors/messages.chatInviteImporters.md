---
title: "messages.chatInviteImporters"
description: "messages.chatInviteImporters attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatInviteImporters.html
---
# Constructor: messages.chatInviteImporters  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](../types/int.md) | Yes|
|importers|Array of [ChatInviteImporter](../types/ChatInviteImporter.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.ChatInviteImporters](../types/messages.ChatInviteImporters.md)


### Example:

```php
$messages_chatInviteImporters = ['_' => 'messages.chatInviteImporters', 'count' => int, 'importers' => [ChatInviteImporter, ChatInviteImporter], 'users' => [User, User]];
```  
