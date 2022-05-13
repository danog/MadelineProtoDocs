---
title: "messages.chatsSlice"
description: "Partial list of chats, more would have to be fetched with pagination"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatsSlice.html
---
# Constructor: messages.chatsSlice  
[Back to constructors index](/API_docs/constructors/index.html)



Partial list of chats, more would have to be fetched with [pagination](https://core.telegram.org/api/offsets)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results that were found server-side (not all are included in `chats`)|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats|



### Type: [messages.Chats](/API_docs/types/messages.Chats.html)


### Example:

```
$messages_chatsSlice = ['_' => 'messages.chatsSlice', 'count' => int, 'chats' => [Chat, Chat]];
```  
