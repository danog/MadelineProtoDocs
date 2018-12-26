---
title: chatParticipants
description: Chat participants
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipants  
[Back to constructors index](index.md)



Chat participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|admin\_id|[int](../types/int.md) | Yes|Admin ID|
|participants|Array of [ChatParticipant](../types/ChatParticipant.md) | Yes|Participants|
|version|[int](../types/int.md) | Yes|Version|



### Type: [ChatParticipants](../types/ChatParticipants.md)


### Example:

```php
$chatParticipants = ['_' => 'chatParticipants', 'chat_id' => int, 'admin_id' => int, 'participants' => [ChatParticipant, ChatParticipant], 'version' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatParticipants", "chat_id": int, "admin_id": int, "participants": [ChatParticipant], "version": int}
```


Or, if you're into Lua:

```lua
chatParticipants={_='chatParticipants', chat_id=int, admin_id=int, participants={ChatParticipant}, version=int}

```


