---
title: "chatParticipantAdmin"
description: "Chat admin"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantAdmin  
[Back to constructors index](index.md)



Chat admin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|inviter\_id|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|Date when the user was added|



### Type: [ChatParticipant](../types/ChatParticipant.md)


### Example:

```php
$chatParticipantAdmin = ['_' => 'chatParticipantAdmin', 'user_id' => long, 'inviter_id' => long, 'date' => int];
```  


Or, if you're into Lua:

```lua
chatParticipantAdmin={_='chatParticipantAdmin', user_id=long, inviter_id=long, date=int}

```


