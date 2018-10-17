---
title: messages.channelMessages
description: messages_channelMessages attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.channelMessages  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pts|[int](../types/int.md) | Yes|
|count|[int](../types/int.md) | Yes|
|messages|Array of [Message](../types/Message.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages\_Messages](../types/messages_Messages.md)


### Example:

```php
$messages_channelMessages = ['_' => 'messages.channelMessages', 'pts' => int, 'count' => int, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.channelMessages", "pts": int, "count": int, "messages": [Message], "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:

```lua
messages_channelMessages={_='messages.channelMessages', pts=int, count=int, messages={Message}, chats={Chat}, users={User}}

```


