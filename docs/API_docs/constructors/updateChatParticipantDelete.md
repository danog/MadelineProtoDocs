---
title: updateChatParticipantDelete
description: A member has left the group.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantDelete  
[Back to constructors index](index.md)



A member has left the group.  
This update is also typically emitted as an [updateNewMessage](updateNewMessage.md) with [messageService](messageService.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Group ID|
|user\_id|[int](../types/int.md) | Yes|ID of the user|
|version|[int](../types/int.md) | Yes|Used in basic groups to reorder updates and make sure that all of them was received.|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipantDelete = ['_' => 'updateChatParticipantDelete', 'chat_id' => int, 'user_id' => int, 'version' => int];
```  


Or, if you're into Lua:

```lua
updateChatParticipantDelete={_='updateChatParticipantDelete', chat_id=int, user_id=int, version=int}

```


