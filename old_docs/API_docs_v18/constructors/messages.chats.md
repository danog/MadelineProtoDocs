---
title: messages.chats
description: List of chats with auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.chats  
[Back to constructors index](index.md)



List of chats with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages.Chats](../types/messages.Chats.md)


### Example:

```php
$messages.chats = ['_' => 'messages.chats', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages.chats={_='messages.chats', chats={Chat}, users={User}}

```


