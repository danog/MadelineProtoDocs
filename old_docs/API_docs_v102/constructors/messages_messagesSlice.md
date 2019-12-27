---
title: messages.messagesSlice
description: Incomplete list of messages and auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.messagesSlice  
[Back to constructors index](index.md)



Incomplete list of messages and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](../types/Bool.md) | Optional|If set, indicates that the results may be inexact|
|count|[int](../types/int.md) | Yes|Total number of messages in the list|
|next\_rate|[int](../types/int.md) | Optional|Rate to use in the `offset_rate` parameter in the next call to [messages.searchGlobal](../methods/messages.searchGlobal.md)|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages\_Messages](../types/messages_Messages.md)


### Example:

```php
$messages_messagesSlice = ['_' => 'messages.messagesSlice', 'inexact' => Bool, 'count' => int, 'next_rate' => int, 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_messagesSlice={_='messages.messagesSlice', inexact=Bool, count=int, next_rate=int, messages={Message}, chats={Chat}, users={User}}

```


