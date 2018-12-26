---
title: chat
description: Chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chat  
[Back to constructors index](index.md)



Chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|title|[string](../types/string.md) | Yes|Title|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Photo|
|participants\_count|[int](../types/int.md) | Yes|Participants count|
|date|[int](../types/int.md) | Yes|Date|
|version|[int](../types/int.md) | Yes|Version|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$chat = ['_' => 'chat', 'id' => int, 'title' => 'string', 'photo' => ChatPhoto, 'participants_count' => int, 'date' => int, 'version' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chat", "id": int, "title": "string", "photo": ChatPhoto, "participants_count": int, "date": int, "version": int}
```


Or, if you're into Lua:

```lua
chat={_='chat', id=int, title='string', photo=ChatPhoto, participants_count=int, date=int, version=int}

```


