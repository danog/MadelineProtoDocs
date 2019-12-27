---
title: messages.statedMessage
description: Stated message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.statedMessage  
[Back to constructors index](index.md)



Stated message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|
|pts|[int](../types/int.md) | Yes|Pts|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [messages.StatedMessage](../types/messages.StatedMessage.md)


### Example:

```php
$messages.statedMessage = ['_' => 'messages.statedMessage', 'message' => Message, 'chats' => [Chat, Chat], 'users' => [User, User], 'pts' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
messages.statedMessage={_='messages.statedMessage', message=Message, chats={Chat}, users={User}, pts=int, seq=int}

```


