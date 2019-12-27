---
title: chatParticipantAdmin
description: Chat admin
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantAdmin  
[Back to constructors index](index.md)



Chat admin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|ID of a group member that is admin|
|inviter\_id|[int](../types/int.md) | Yes|ID of the user that added the member to the group|
|date|[int](../types/int.md) | Yes|Date when the user was added|



### Type: [ChatParticipant](../types/ChatParticipant.md)


### Example:

```php
$chatParticipantAdmin = ['_' => 'chatParticipantAdmin', 'user_id' => int, 'inviter_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
chatParticipantAdmin={_='chatParticipantAdmin', user_id=int, inviter_id=int, date=int}

```


