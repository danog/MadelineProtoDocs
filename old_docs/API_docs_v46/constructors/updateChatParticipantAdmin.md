---
title: updateChatParticipantAdmin
description: Update chat participant admin
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantAdmin  
[Back to constructors index](index.md)



Update chat participant admin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|is\_admin|[Bool](../types/Bool.md) | Yes|Is admin?|
|version|[int](../types/int.md) | Yes|Version|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatParticipantAdmin = ['_' => 'updateChatParticipantAdmin', 'chat_id' => int, 'user_id' => int, 'is_admin' => Bool, 'version' => int];
```  


Or, if you're into Lua:

```lua
updateChatParticipantAdmin={_='updateChatParticipantAdmin', chat_id=int, user_id=int, is_admin=Bool, version=int}

```


