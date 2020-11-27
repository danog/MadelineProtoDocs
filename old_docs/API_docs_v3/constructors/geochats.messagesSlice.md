---
title: geochats.messagesSlice
description: geochats.messagesSlice attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/geochats_messagesSlice.html
---
# Constructor: geochats.messagesSlice  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](../types/int.md) | Yes|
|messages|Array of [GeoChatMessage](../types/GeoChatMessage.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [geochats.Messages](../types/geochats.Messages.md)


### Example:

```php
$geochats_messagesSlice = ['_' => 'geochats.messagesSlice', 'count' => int, 'messages' => [GeoChatMessage, GeoChatMessage], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
geochats_messagesSlice={_='geochats.messagesSlice', count=int, messages={GeoChatMessage}, chats={Chat}, users={User}}

```


