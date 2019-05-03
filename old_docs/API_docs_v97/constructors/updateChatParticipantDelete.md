---
title: updateChatParticipantDelete
description: Update chat participant delete
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantDelete  
[Back to constructors index](index.md)



Update chat participant delete

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|version|[int](../types/int.md) | Yes|Version|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipantDelete = ['_' => 'updateChatParticipantDelete', 'chat_id' => int, 'user_id' => int, 'version' => int];
```  


Or, if you're into Lua:

```lua
updateChatParticipantDelete={_='updateChatParticipantDelete', chat_id=int, user_id=int, version=int}

```


