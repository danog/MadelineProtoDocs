---
title: "messages.chats"
description: "List of chats with auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chats.html
---
# Constructor: messages.chats  
[Back to constructors index](/API_docs/constructors/index.html)



List of chats with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|List of chats|



### Type: [messages.Chats](/API_docs/types/messages.Chats.html)


### Example:

```
$messages_chats = ['_' => 'messages.chats', 'chats' => [Chat, Chat]];
```  
