---
title: messages.chatFull
description: Extended info on chat and auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.chatFull  
[Back to constructors index](index.md)



Extended info on chat and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|full\_chat|[ChatFull](../types/ChatFull.md) | Yes|Extended info on a chat|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages\_ChatFull](../types/messages_ChatFull.md)


### Example:

```php
$messages_chatFull = ['_' => 'messages.chatFull', 'full_chat' => ChatFull, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_chatFull={_='messages.chatFull', full_chat=ChatFull, chats={Chat}, users={User}}

```


