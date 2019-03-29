---
title: messages.statedMessagesLinks
description: Stated messages links
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.statedMessagesLinks  
[Back to constructors index](index.md)



Stated messages links

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [Message](../types/Message.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|
|links|Array of [contacts\_Link](../types/contacts_Link.md) | Yes|Links|
|pts|[int](../types/int.md) | Yes|Pts|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [messages\_StatedMessages](../types/messages_StatedMessages.md)


### Example:

```php
$messages_statedMessagesLinks = ['_' => 'messages.statedMessagesLinks', 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User], 'links' => [contacts_Link, contacts_Link], 'pts' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
messages_statedMessagesLinks={_='messages.statedMessagesLinks', messages={Message}, chats={Chat}, users={User}, links={contacts_Link}, pts=int, seq=int}

```


