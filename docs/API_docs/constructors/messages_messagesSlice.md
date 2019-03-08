---
title: messages.messagesSlice
description: Messages slice
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.messagesSlice  
[Back to constructors index](index.md)



Messages slice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](../types/Bool.md) | Optional|Inexact?|
|count|[int](../types/int.md) | Yes|Count|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages\_Messages](../types/messages_Messages.md)


### Example:

```php
$messages_messagesSlice = ['_' => 'messages.messagesSlice', 'inexact' => Bool, 'count' => int, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.messagesSlice", "inexact": Bool, "count": int, "messages": [Message], "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:

```lua
messages_messagesSlice={_='messages.messagesSlice', inexact=Bool, count=int, messages={Message}, chats={Chat}, users={User}}

```


