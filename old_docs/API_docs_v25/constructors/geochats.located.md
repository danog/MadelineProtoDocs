---
title: geochats.located
description: Located
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geochats.located  
[Back to constructors index](index.md)



Located

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|results|Array of [ChatLocated](../types/ChatLocated.md) | Yes|Results|
|messages|Array of [GeoChatMessage](../types/GeoChatMessage.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [geochats.Located](../types/geochats.Located.md)


### Example:

```php
$geochats.located = ['_' => 'geochats.located', 'results' => [ChatLocated, ChatLocated], 'messages' => [GeoChatMessage, GeoChatMessage], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
geochats.located={_='geochats.located', results={ChatLocated}, messages={GeoChatMessage}, chats={Chat}, users={User}}

```


