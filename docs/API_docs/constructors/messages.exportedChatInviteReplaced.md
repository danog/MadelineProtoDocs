---
title: "messages.exportedChatInviteReplaced"
description: "messages.exportedChatInviteReplaced attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_exportedChatInviteReplaced.html
---
# Constructor: messages.exportedChatInviteReplaced  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|
|new\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.ExportedChatInvite](../types/messages.ExportedChatInvite.md)


### Example:

```php
$messages_exportedChatInviteReplaced = ['_' => 'messages.exportedChatInviteReplaced', 'invite' => ExportedChatInvite, 'new_invite' => ExportedChatInvite, 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_exportedChatInviteReplaced={_='messages.exportedChatInviteReplaced', invite=ExportedChatInvite, new_invite=ExportedChatInvite, users={User}}

```


