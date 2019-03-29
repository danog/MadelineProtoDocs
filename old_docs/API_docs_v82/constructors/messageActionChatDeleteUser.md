---
title: messageActionChatDeleteUser
description: Message action chat delete user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatDeleteUser  
[Back to constructors index](index.md)



Message action chat delete user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatDeleteUser = ['_' => 'messageActionChatDeleteUser', 'user_id' => int];
```  


Or, if you're into Lua:

```lua
messageActionChatDeleteUser={_='messageActionChatDeleteUser', user_id=int}

```


