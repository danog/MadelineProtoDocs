---
title: "messages.inactiveChats"
description: "Inactive chat list"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_inactiveChats.html
---
# Constructor: messages.inactiveChats  
[Back to constructors index](index.md)



Inactive chat list

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dates|Array of [int](../types/int.md) | Yes|When was the chat last active|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chat list|
|users|Array of [User](../types/User.md) | Yes|Users mentioned in the chat list|



### Type: [messages.InactiveChats](../types/messages.InactiveChats.md)


### Example:

```php
$messages_inactiveChats = ['_' => 'messages.inactiveChats', 'dates' => [int, int], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_inactiveChats={_='messages.inactiveChats', dates={int}, chats={Chat}, users={User}}

```


