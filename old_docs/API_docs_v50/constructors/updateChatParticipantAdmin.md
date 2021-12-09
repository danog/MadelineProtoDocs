---
title: updateChatParticipantAdmin
description: Admin permissions of a user in a [legacy group](https://core.telegram.org/api/channel) were changed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantAdmin  
[Back to constructors index](index.md)



Admin permissions of a user in a [legacy group](https://core.telegram.org/api/channel) were changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](../types/long.md) | Yes|
|user\_id|[long](../types/long.md) | Yes|
|is\_admin|[Bool](../types/Bool.md) | Yes|Whether the user was rendered admin|
|version|[int](../types/int.md) | Yes|Used in basic groups to reorder updates and make sure that all of them was received.|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipantAdmin = ['_' => 'updateChatParticipantAdmin', 'chat_id' => long, 'user_id' => long, 'is_admin' => Bool, 'version' => int];
```  


Or, if you're into Lua:

```lua
updateChatParticipantAdmin={_='updateChatParticipantAdmin', chat_id=long, user_id=long, is_admin=Bool, version=int}

```


