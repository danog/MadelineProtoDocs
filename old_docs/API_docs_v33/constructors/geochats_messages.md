---
title: geochats.messages
description: Messages
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geochats.messages  
[Back to constructors index](index.md)



Messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|messages|Array of [GeoChatMessage](../types/GeoChatMessage.md) | Yes|Messages|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [geochats\_Messages](../types/geochats_Messages.md)


### Example:

```php
$geochats_messages = ['_' => 'geochats.messages', 'messages' => [GeoChatMessage, GeoChatMessage], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "geochats.messages", "messages": [GeoChatMessage], "chats": [Chat], "users": [User]}
```


Or, if you're into Lua:

```lua
geochats_messages={_='geochats.messages', messages={GeoChatMessage}, chats={Chat}, users={User}}

```


