---
title: chatParticipant
description: Group member.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipant  
[Back to constructors index](index.md)



Group member.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|Member user ID|
|inviter\_id|[int](../types/int.md) | Yes|ID of the user that added the member to the group|
|date|[int](../types/int.md) | Yes|Date added to the group|



### Type: [ChatParticipant](../types/ChatParticipant.md)


### Example:

```php
$chatParticipant = ['_' => 'chatParticipant', 'user_id' => int, 'inviter_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
chatParticipant={_='chatParticipant', user_id=int, inviter_id=int, date=int}

```


