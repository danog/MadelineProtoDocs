---
title: messages.channelMessages
description: Channel messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.channelMessages  
[Back to constructors index](index.md)



Channel messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](../types/int.md) | Yes|Pts|
|count|[int](../types/int.md) | Yes|Count|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|collapsed|Array of [MessageGroup](../types/MessageGroup.md) | Optional|Collapsed|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages\_Messages](../types/messages_Messages.md)


### Example:

```php
$messages_channelMessages = ['_' => 'messages.channelMessages', 'pts' => int, 'count' => int, 'messages' => [Message, Message], 'collapsed' => [MessageGroup, MessageGroup], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_channelMessages={_='messages.channelMessages', pts=int, count=int, messages={Message}, collapsed={MessageGroup}, chats={Chat}, users={User}}

```


