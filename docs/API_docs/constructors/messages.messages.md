---
title: "messages.messages"
description: "Full list of messages with auxilary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_messages.html
---
# Constructor: messages.messages  
[Back to constructors index](index.md)



Full list of messages with auxilary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [Message](../types/Message.md) | Yes|List of messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|List of chats mentioned in dialogs|
|users|Array of [User](../types/User.md) | Yes|List of users mentioned in messages and chats|



### Type: [messages.Messages](../types/messages.Messages.md)


### Example:

```php
$messages_messages = ['_' => 'messages.messages', 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_messages={_='messages.messages', messages={Message}, chats={Chat}, users={User}}

```


