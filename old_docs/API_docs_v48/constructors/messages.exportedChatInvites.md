---
title: messages.exportedChatInvites
description: messages.exportedChatInvites attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_exportedChatInvites.html
---
# Constructor: messages.exportedChatInvites  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](../types/int.md) | Yes|
|invites|Array of [ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.ExportedChatInvites](../types/messages.ExportedChatInvites.md)


### Example:

```php
$messages_exportedChatInvites = ['_' => 'messages.exportedChatInvites', 'count' => int, 'invites' => [ExportedChatInvite, ExportedChatInvite], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_exportedChatInvites={_='messages.exportedChatInvites', count=int, invites={ExportedChatInvite}, users={User}}

```


