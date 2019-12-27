---
title: chatInviteAlready
description: The user has already joined this chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInviteAlready  
[Back to constructors index](index.md)



The user has already joined this chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat|[Chat](../types/Chat.md) | Optional|The chat connected to the invite|



### Type: [ChatInvite](../types/ChatInvite.md)


### Example:

```php
$chatInviteAlready = ['_' => 'chatInviteAlready', 'chat' => Chat];
```  


Or, if you're into Lua:

```lua
chatInviteAlready={_='chatInviteAlready', chat=Chat}

```


