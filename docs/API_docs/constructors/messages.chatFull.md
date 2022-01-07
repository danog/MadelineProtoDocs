---
title: "messages.chatFull"
description: "Extended info on chat and auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatFull.html
---
# Constructor: messages.chatFull  
[Back to constructors index](/API_docs/constructors/index.html)



Extended info on chat and auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|full\_chat|[ChatFull](/API_docs/types/ChatFull.html) | Yes|Extended info on a chat|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|List containing basic info on chat|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of users mentioned above|



### Type: [messages.ChatFull](/API_docs/types/messages.ChatFull.html)


### Example:

```php
$messages_chatFull = ['_' => 'messages.chatFull', 'full_chat' => ChatFull, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
