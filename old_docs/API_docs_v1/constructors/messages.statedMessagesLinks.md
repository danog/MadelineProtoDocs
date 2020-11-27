---
title: messages.statedMessagesLinks
description: messages.statedMessagesLinks attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_statedMessagesLinks.html
---
# Constructor: messages.statedMessagesLinks  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|messages|Array of [Message](../types/Message.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|
|links|Array of [contacts.Link](../constructors/contacts.Link.md) | Yes|
|pts|[int](../types/int.md) | Yes|
|seq|[int](../types/int.md) | Yes|



### Type: [messages.StatedMessages](../types/messages.StatedMessages.md)


### Example:

```php
$messages_statedMessagesLinks = ['_' => 'messages.statedMessagesLinks', 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User], 'links' => [contacts.Link, contacts.Link], 'pts' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
messages_statedMessagesLinks={_='messages.statedMessagesLinks', messages={Message}, chats={Chat}, users={User}, links={contacts.Link}, pts=int, seq=int}

```


