---
title: messages.chatFull
description: Chat full
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.chatFull  
[Back to constructors index](index.md)



Chat full

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|full\_chat|[ChatFull](../types/ChatFull.md) | Yes|Full chat|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages\_ChatFull](../types/messages_ChatFull.md)


### Example:

```php
$messages_chatFull = ['_' => 'messages.chatFull', 'full_chat' => ChatFull, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.chatFull", "full_chat": ChatFull, "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:

```lua
messages_chatFull={_='messages.chatFull', full_chat=ChatFull, chats={Chat}, users={User}}

```


