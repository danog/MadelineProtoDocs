---
title: chatParticipantsForbidden
description: Chat participants forbidden
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantsForbidden  
[Back to constructors index](index.md)



Chat participants forbidden

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|self\_participant|[ChatParticipant](../types/ChatParticipant.md) | Optional|Self participant|



### Type: [ChatParticipants](../types/ChatParticipants.md)


### Example:

```php
$chatParticipantsForbidden = ['_' => 'chatParticipantsForbidden', 'chat_id' => int, 'self_participant' => ChatParticipant];
```  


Or, if you're into Lua:

```lua
chatParticipantsForbidden={_='chatParticipantsForbidden', chat_id=int, self_participant=ChatParticipant}

```


