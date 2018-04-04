---
title: messages.chats
description: messages_chats attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: messages.chats  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages\_Chats](../types/messages_Chats.md)


### Example:

```
$messages_chats = ['_' => 'messages.chats', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.chats", "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:  


```
messages_chats={_='messages.chats', chats={Chat}, users={User}}

```


