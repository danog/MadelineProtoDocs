---
title: geochats.statedMessage
description: geochats.statedMessage attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/geochats_statedMessage.html
---
# Constructor: geochats.statedMessage  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|message|[GeoChatMessage](../types/GeoChatMessage.md) | Optional|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|
|seq|[int](../types/int.md) | Yes|



### Type: [geochats.StatedMessage](../types/geochats.StatedMessage.md)


### Example:

```php
$geochats_statedMessage = ['_' => 'geochats.statedMessage', 'message' => GeoChatMessage, 'chats' => [Chat, Chat], 'users' => [User, User], 'seq' => int];
```  


Or, if you're into Lua:

```lua
geochats_statedMessage={_='geochats.statedMessage', message=GeoChatMessage, chats={Chat}, users={User}, seq=int}

```


