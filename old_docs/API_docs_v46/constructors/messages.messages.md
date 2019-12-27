---
title: messages.messages
description: Full list of messages with auxilary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.messages  
[Back to constructors index](index.md)



Full list of messages with auxilary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [messages.Messages](../types/messages.Messages.md)


### Example:

```php
$messages.messages = ['_' => 'messages.messages', 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages.messages={_='messages.messages', messages={Message}, chats={Chat}, users={User}}

```


