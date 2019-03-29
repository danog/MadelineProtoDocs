---
title: updateChatParticipantAdd
description: Update chat participant add
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantAdd  
[Back to constructors index](index.md)



Update chat participant add

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|inviter\_id|[int](../types/int.md) | Yes|Inviter ID|
|version|[int](../types/int.md) | Yes|Version|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipantAdd = ['_' => 'updateChatParticipantAdd', 'chat_id' => int, 'user_id' => int, 'inviter_id' => int, 'version' => int];
```  


Or, if you're into Lua:

```lua
updateChatParticipantAdd={_='updateChatParticipantAdd', chat_id=int, user_id=int, inviter_id=int, version=int}

```


