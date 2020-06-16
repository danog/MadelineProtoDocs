---
title: messages.statedMessage
description: messages.statedMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_statedMessage.html
---
# Constructor: messages.statedMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|message|[Message](../types/Message.md) | Optional|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|
|pts|[int](../types/int.md) | Yes|
|pts\_count|[int](../types/int.md) | Yes|



### Type: [messages.StatedMessage](../types/messages.StatedMessage.md)


### Example:

```php
$messages.statedMessage = ['_' => 'messages.statedMessage', 'message' => Message, 'chats' => [Chat, Chat], 'users' => [User, User], 'pts' => int, 'pts_count' => int];
```  


Or, if you're into Lua:

```lua
messages.statedMessage={_='messages.statedMessage', message=Message, chats={Chat}, users={User}, pts=int, pts_count=int}

```


