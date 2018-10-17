---
title: updateChatParticipantDelete
description: updateChatParticipantDelete attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantDelete  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|
|user\_id|[int](../types/int.md) | Yes|
|version|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipantDelete = ['_' => 'updateChatParticipantDelete', 'chat_id' => int, 'user_id' => int, 'version' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChatParticipantDelete", "chat_id": int, "user_id": int, "version": int}
```


Or, if you're into Lua:

```lua
updateChatParticipantDelete={_='updateChatParticipantDelete', chat_id=int, user_id=int, version=int}

```


