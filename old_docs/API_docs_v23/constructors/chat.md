---
title: chat
description: Info about a group
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chat  
[Back to constructors index](index.md)



Info about a group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID of the group|
|title|[string](../types/string.md) | Yes|Title|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Chat photo|
|participants\_count|[int](../types/int.md) | Yes|Participant count|
|date|[int](../types/int.md) | Yes|Date of creation of the group|
|left|[Bool](../types/Bool.md) | Yes|Left?|
|version|[int](../types/int.md) | Yes|Used in basic groups to reorder updates and make sure that all of them were received.|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$chat = ['_' => 'chat', 'id' => int, 'title' => 'string', 'photo' => ChatPhoto, 'participants_count' => int, 'date' => int, 'left' => Bool, 'version' => int];
```  


Or, if you're into Lua:

```lua
chat={_='chat', id=int, title='string', photo=ChatPhoto, participants_count=int, date=int, left=Bool, version=int}

```


