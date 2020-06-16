---
title: chatParticipantsForbidden
description: Info on members is unavailable
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantsForbidden  
[Back to constructors index](index.md)



Info on members is unavailable

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Group ID|
|self\_participant|[ChatParticipant](../types/ChatParticipant.md) | Optional|Info about the group membership of the current user|



### Type: [ChatParticipants](../types/ChatParticipants.md)


### Example:

```php
$chatParticipantsForbidden = ['_' => 'chatParticipantsForbidden', 'chat_id' => int, 'self_participant' => ChatParticipant];
```  


Or, if you're into Lua:

```lua
chatParticipantsForbidden={_='chatParticipantsForbidden', chat_id=int, self_participant=ChatParticipant}

```


