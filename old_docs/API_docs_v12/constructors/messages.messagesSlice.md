---
title: messages.messagesSlice
description: Incomplete list of messages and auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messagesSlice.html
---
# Constructor: messages.messagesSlice  
[Back to constructors index](index.md)



Incomplete list of messages and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Total number of messages in the list|
|messages|Array of [Message](../types/Message.md) | Yes|List of messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|List of chats mentioned in messages|
|users|Array of [User](../types/User.md) | Yes|List of users mentioned in messages and chats|



### Type: [messages.Messages](../types/messages.Messages.md)


### Example:

```php
$messages.messagesSlice = ['_' => 'messages.messagesSlice', 'count' => int, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages.messagesSlice={_='messages.messagesSlice', count=int, messages={Message}, chats={Chat}, users={User}}

```


