---
title: chatInvitePeek
description: chatInvitePeek attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInvitePeek  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat|[Chat](../types/Chat.md) | Optional|
|expires|[int](../types/int.md) | Yes|



### Type: [ChatInvite](../types/ChatInvite.md)


### Example:

```php
$chatInvitePeek = ['_' => 'chatInvitePeek', 'chat' => Chat, 'expires' => int];
```  


Or, if you're into Lua:

```lua
chatInvitePeek={_='chatInvitePeek', chat=Chat, expires=int}

```


