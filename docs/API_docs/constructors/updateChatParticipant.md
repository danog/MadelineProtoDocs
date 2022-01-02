---
title: "updateChatParticipant"
description: "updateChatParticipant attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipant  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|
|actor\_id|[long](../types/long.md) | Yes|
|user\_id|[long](../types/long.md) | Yes|
|prev\_participant|[ChatParticipant](../types/ChatParticipant.md) | Optional|
|new\_participant|[ChatParticipant](../types/ChatParticipant.md) | Optional|
|invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Optional|
|qts|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipant = ['_' => 'updateChatParticipant', 'chat_id' => long, 'date' => int, 'actor_id' => long, 'user_id' => long, 'prev_participant' => ChatParticipant, 'new_participant' => ChatParticipant, 'invite' => ExportedChatInvite, 'qts' => int];
```  


Or, if you're into Lua:

```lua
updateChatParticipant={_='updateChatParticipant', chat_id=long, date=int, actor_id=long, user_id=long, prev_participant=ChatParticipant, new_participant=ChatParticipant, invite=ExportedChatInvite, qts=int}

```


