---
title: geochats.messagesSlice
description: Messages slice
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geochats.messagesSlice  
[Back to constructors index](index.md)



Messages slice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Count|
|messages|Array of [GeoChatMessage](../types/GeoChatMessage.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [geochats\_Messages](../types/geochats_Messages.md)


### Example:

```php
$geochats_messagesSlice = ['_' => 'geochats.messagesSlice', 'count' => int, 'messages' => [GeoChatMessage, GeoChatMessage], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "geochats.messagesSlice", "count": int, "messages": [GeoChatMessage], "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:

```lua
geochats_messagesSlice={_='geochats.messagesSlice', count=int, messages={GeoChatMessage}, chats={Chat}, users={User}}

```


