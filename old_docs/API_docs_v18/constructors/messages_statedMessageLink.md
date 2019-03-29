---
title: messages.statedMessageLink
description: Stated message link
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.statedMessageLink  
[Back to constructors index](index.md)



Stated message link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|
|links|Array of [contacts\_Link](../types/contacts_Link.md) | Yes|Links|
|pts|[int](../types/int.md) | Yes|Pts|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [messages\_StatedMessage](../types/messages_StatedMessage.md)


### Example:

```php
$messages_statedMessageLink = ['_' => 'messages.statedMessageLink', 'message' => Message, 'chats' => [Chat, Chat], 'users' => [User, User], 'links' => [contacts_Link, contacts_Link], 'pts' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
messages_statedMessageLink={_='messages.statedMessageLink', message=Message, chats={Chat}, users={User}, links={contacts_Link}, pts=int, seq=int}

```


