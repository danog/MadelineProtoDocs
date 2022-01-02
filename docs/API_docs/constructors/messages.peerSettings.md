---
title: "messages.peerSettings"
description: "messages.peerSettings attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_peerSettings.html
---
# Constructor: messages.peerSettings  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|settings|[PeerSettings](../types/PeerSettings.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.PeerSettings](../types/messages.PeerSettings.md)


### Example:

```php
$messages_peerSettings = ['_' => 'messages.peerSettings', 'settings' => PeerSettings, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
messages_peerSettings={_='messages.peerSettings', settings=PeerSettings, chats={Chat}, users={User}}

```


