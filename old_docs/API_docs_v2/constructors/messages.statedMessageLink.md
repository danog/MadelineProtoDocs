---
title: messages.statedMessageLink
description: messages.statedMessageLink attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_statedMessageLink.html
---
# Constructor: messages.statedMessageLink  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|message|[Message](../types/Message.md) | Optional|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|
|pts|[int](../types/int.md) | Yes|
|pts\_count|[int](../types/int.md) | Yes|
|links|Array of [contacts.Link](../constructors/contacts.Link.md) | Yes|
|seq|[int](../types/int.md) | Yes|



### Type: [messages.StatedMessage](../types/messages.StatedMessage.md)


### Example:

```php
$messages_statedMessageLink = ['_' => 'messages.statedMessageLink', 'message' => Message, 'chats' => [Chat, Chat], 'users' => [User, User], 'pts' => int, 'pts_count' => int, 'links' => [contacts.Link, contacts.Link], 'seq' => int];
```  


Or, if you're into Lua:

```lua
messages_statedMessageLink={_='messages.statedMessageLink', message=Message, chats={Chat}, users={User}, pts=int, pts_count=int, links={contacts.Link}, seq=int}

```


