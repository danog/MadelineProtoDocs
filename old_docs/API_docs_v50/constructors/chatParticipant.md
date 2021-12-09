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
|user\_id|[long](../types/long.md) | Yes|
|inviter\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|Date added to the group|



### Type: [ChatParticipant](../types/ChatParticipant.md)


### Example:

```php
$chatParticipant = ['_' => 'chatParticipant', 'user_id' => long, 'inviter_id' => long, 'date' => int];
```  


Or, if you're into Lua:

```lua
chatParticipant={_='chatParticipant', user_id=long, inviter_id=long, date=int}

```


