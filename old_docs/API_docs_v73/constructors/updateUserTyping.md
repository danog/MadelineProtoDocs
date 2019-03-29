---
title: updateUserTyping
description: Update user typing
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserTyping  
[Back to constructors index](index.md)



Update user typing

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|action|[SendMessageAction](../types/SendMessageAction.md) | Yes|Action|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserTyping = ['_' => 'updateUserTyping', 'user_id' => int, 'action' => SendMessageAction];
```  


Or, if you're into Lua:

```lua
updateUserTyping={_='updateUserTyping', user_id=int, action=SendMessageAction}

```


