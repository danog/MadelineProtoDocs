---
title: chatParticipant
description: Chat participant
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipant  
[Back to constructors index](index.md)



Chat participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|inviter\_id|[int](../types/int.md) | Yes|Inviter ID|
|date|[int](../types/int.md) | Yes|Date|



### Type: [ChatParticipant](../types/ChatParticipant.md)


### Example:

```php
$chatParticipant = ['_' => 'chatParticipant', 'user_id' => int, 'inviter_id' => int, 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatParticipant", "user_id": int, "inviter_id": int, "date": int}
```


Or, if you're into Lua:

```lua
chatParticipant={_='chatParticipant', user_id=int, inviter_id=int, date=int}

```


