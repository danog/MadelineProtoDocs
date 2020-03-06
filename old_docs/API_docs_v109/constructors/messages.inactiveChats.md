---
title: messages.inactiveChats
description: messages.inactiveChats attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_inactiveChats.html
---
# Constructor: messages.inactiveChats  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dates|Array of [int](../types/int.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.InactiveChats](../types/messages.InactiveChats.md)


### Example:

```php
$messages.inactiveChats = ['_' => 'messages.inactiveChats', 'dates' => [int, int], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages.inactiveChats={_='messages.inactiveChats', dates={int}, chats={Chat}, users={User}}

```


