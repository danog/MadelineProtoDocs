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
|pts|[int](../types/int.md) | Yes|Pts|
|pts\_count|[int](../types/int.md) | Yes|Pts count|
|links|Array of [contacts\_Link](../types/contacts_Link.md) | Yes|Links|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [messages\_StatedMessages](../types/messages_StatedMessages.md)


### Example:

```php
$messages_statedMessagesLinks = ['_' => 'messages.statedMessagesLinks', 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User], 'pts' => int, 'pts_count' => int, 'links' => [contacts_Link, contacts_Link], 'seq' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.statedMessagesLinks", "messages": [Message], "chats": [Chat], "users": [User], "pts": int, "pts_count": int, "links": [contacts_Link], "seq": int}
```


Or, if you're into Lua:

```lua
messages_statedMessagesLinks={_='messages.statedMessagesLinks', messages={Message}, chats={Chat}, users={User}, pts=int, pts_count=int, links={contacts_Link}, seq=int}

```


