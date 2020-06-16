---
title: chatParticipants
description: Group members.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipants  
[Back to constructors index](index.md)



Group members.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Group identifier|
|admin\_id|[int](../types/int.md) | Yes|
|participants|Array of [ChatParticipant](../types/ChatParticipant.md) | Yes|List of group members|
|version|[int](../types/int.md) | Yes|Group version number|



### Type: [ChatParticipants](../types/ChatParticipants.md)


### Example:

```php
$chatParticipants = ['_' => 'chatParticipants', 'chat_id' => int, 'admin_id' => int, 'participants' => [ChatParticipant, ChatParticipant], 'version' => int];
```  


Or, if you're into Lua:

```lua
chatParticipants={_='chatParticipants', chat_id=int, admin_id=int, participants={ChatParticipant}, version=int}

```


