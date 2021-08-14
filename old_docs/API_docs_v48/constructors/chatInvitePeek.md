---
title: chatInvitePeek
description: A chat invitation that also allows peeking into the group to read messages without joining it.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInvitePeek  
[Back to constructors index](index.md)



A chat invitation that also allows peeking into the group to read messages without joining it.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat|[Chat](../types/Chat.md) | Optional|Chat information|
|expires|[int](../types/int.md) | Yes|Read-only anonymous access to this group will be revoked at this date|



### Type: [ChatInvite](../types/ChatInvite.md)


### Example:

```php
$chatInvitePeek = ['_' => 'chatInvitePeek', 'chat' => Chat, 'expires' => int];
```  


Or, if you're into Lua:

```lua
chatInvitePeek={_='chatInvitePeek', chat=Chat, expires=int}

```


