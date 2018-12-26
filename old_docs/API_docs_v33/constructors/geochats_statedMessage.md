---
title: geochats.statedMessage
description: Stated message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geochats.statedMessage  
[Back to constructors index](index.md)



Stated message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[GeoChatMessage](../types/GeoChatMessage.md) | Optional|Message|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [geochats\_StatedMessage](../types/geochats_StatedMessage.md)


### Example:

```php
$geochats_statedMessage = ['_' => 'geochats.statedMessage', 'message' => GeoChatMessage, 'chats' => [Chat, Chat], 'users' => [User, User], 'seq' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "geochats.statedMessage", "message": GeoChatMessage, "chats": [Chat], "users": [User], "seq": int}
```


Or, if you're into Lua:

```lua
geochats_statedMessage={_='geochats.statedMessage', message=GeoChatMessage, chats={Chat}, users={User}, seq=int}

```


