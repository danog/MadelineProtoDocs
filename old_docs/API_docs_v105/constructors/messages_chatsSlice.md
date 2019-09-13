---
title: messages.chatsSlice
description: Chats slice
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.chatsSlice  
[Back to constructors index](index.md)



Chats slice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Count|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|



### Type: [messages\_Chats](../types/messages_Chats.md)


### Example:

```php
$messages_chatsSlice = ['_' => 'messages.chatsSlice', 'count' => int, 'chats' => [Chat, Chat]];
```  


Or, if you're into Lua:

```lua
messages_chatsSlice={_='messages.chatsSlice', count=int, chats={Chat}}

```


