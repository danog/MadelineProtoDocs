---
title: "messages.chatFull"
description: "Full info about a channel, supergroup, gigagroup or basic group."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatFull.html
---
# Constructor: messages.chatFull  
[Back to constructors index](/API_docs/constructors/index.html)



Full info about a [channel](https://core.telegram.org/api/channel#channels), [supergroup](https://core.telegram.org/api/channel#supergroups), [gigagroup](https://core.telegram.org/api/channel#gigagroups) or [basic group](https://core.telegram.org/api/channel#basic-groups).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|full\_chat|[ChatFull](/API_docs/types/ChatFull.html) | Yes|Full info|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [messages.ChatFull](/API_docs/types/messages.ChatFull.html)


### Example:

```
$messages_chatFull = ['_' => 'messages.chatFull', 'full_chat' => ChatFull, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
