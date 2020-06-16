---
title: messageActionChatDeleteUser
description: User left the group.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatDeleteUser  
[Back to constructors index](index.md)



User left the group.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|Leaving user ID|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatDeleteUser = ['_' => 'messageActionChatDeleteUser', 'user_id' => int];
```  


Or, if you're into Lua:

```lua
messageActionChatDeleteUser={_='messageActionChatDeleteUser', user_id=int}

```


