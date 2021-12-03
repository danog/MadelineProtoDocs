---
title: updateChatParticipant
description: updateChatParticipant attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipant  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|
|actor\_id|[int](../types/int.md) | Yes|
|user\_id|[int](../types/int.md) | Yes|
|prev\_participant|[ChatParticipant](../types/ChatParticipant.md) | Optional|
|new\_participant|[ChatParticipant](../types/ChatParticipant.md) | Optional|
|invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Optional|
|qts|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipant = ['_' => 'updateChatParticipant', 'chat_id' => int, 'date' => int, 'actor_id' => int, 'user_id' => int, 'prev_participant' => ChatParticipant, 'new_participant' => ChatParticipant, 'invite' => ExportedChatInvite, 'qts' => int];
```  


Or, if you're into Lua:

```lua
updateChatParticipant={_='updateChatParticipant', chat_id=int, date=int, actor_id=int, user_id=int, prev_participant=ChatParticipant, new_participant=ChatParticipant, invite=ExportedChatInvite, qts=int}

```


