---
title: messages.chats
description: Chats
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.chats  
[Back to constructors index](index.md)



Chats

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|



### Type: [messages\_Chats](../types/messages_Chats.md)


### Example:

```php
$messages_chats = ['_' => 'messages.chats', 'chats' => [Chat, Chat]];
```  


Or, if you're into Lua:

```lua
messages_chats={_='messages.chats', chats={Chat}}

```


