---
title: geochats.located
description: geochats.located attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/geochats_located.html
---
# Constructor: geochats.located  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|results|Array of [ChatLocated](../types/ChatLocated.md) | Yes|
|messages|Array of [GeoChatMessage](../types/GeoChatMessage.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [geochats.Located](../types/geochats.Located.md)


### Example:

```php
$geochats_located = ['_' => 'geochats.located', 'results' => [ChatLocated, ChatLocated], 'messages' => [GeoChatMessage, GeoChatMessage], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
geochats_located={_='geochats.located', results={ChatLocated}, messages={GeoChatMessage}, chats={Chat}, users={User}}

```


