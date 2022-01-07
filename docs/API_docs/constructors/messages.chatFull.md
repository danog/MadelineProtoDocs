---
title: "messages.chatFull"
description: "Extended info on chat and auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatFull.html
---
# Constructor: messages.chatFull  
[Back to constructors index](index.md)



Extended info on chat and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|full\_chat|[ChatFull](../types/ChatFull.md) | Yes|Extended info on a chat|
|chats|Array of [Chat](../types/Chat.md) | Yes|List containing basic info on chat|
|users|Array of [User](../types/User.md) | Yes|List of users mentioned above|



### Type: [messages.ChatFull](../types/messages.ChatFull.md)


### Example:

```php
$messages_chatFull = ['_' => 'messages.chatFull', 'full_chat' => ChatFull, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
