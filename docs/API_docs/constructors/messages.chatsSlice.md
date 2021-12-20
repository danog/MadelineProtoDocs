---
title: "messages.chatsSlice"
description: "Partial list of chats, more would have to be fetched with pagination"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_chatsSlice.html
---
# Constructor: messages.chatsSlice  
[Back to constructors index](index.md)



Partial list of chats, more would have to be fetched with [pagination](https://core.telegram.org/api/offsets)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Total number of results that were found server-side (not all are included in `chats`)|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|



### Type: [messages.Chats](../types/messages.Chats.md)


### Example:

```php
$messages_chatsSlice = ['_' => 'messages.chatsSlice', 'count' => int, 'chats' => [Chat, Chat]];
```  


Or, if you're into Lua:

```lua
messages_chatsSlice={_='messages.chatsSlice', count=int, chats={Chat}}

```


