---
title: "messages.exportedChatInvite"
description: "messages.exportedChatInvite attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_exportedChatInvite.html
---
# Constructor: messages.exportedChatInvite  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.ExportedChatInvite](../types/messages.ExportedChatInvite.md)


### Example:

```php
$messages_exportedChatInvite = ['_' => 'messages.exportedChatInvite', 'invite' => ExportedChatInvite, 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_exportedChatInvite={_='messages.exportedChatInvite', invite=ExportedChatInvite, users={User}}

```


