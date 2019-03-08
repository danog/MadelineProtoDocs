---
title: updateChatUserTyping
description: Update chat user typing
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatUserTyping  
[Back to constructors index](index.md)



Update chat user typing

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|
|user\_id|[int](../types/int.md) | Yes|User ID|
|action|[SendMessageAction](../types/SendMessageAction.md) | Yes|Action|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateChatUserTyping = ['_' => 'updateChatUserTyping', 'chat_id' => int, 'user_id' => int, 'action' => SendMessageAction];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChatUserTyping", "chat_id": int, "user_id": int, "action": SendMessageAction}
```


Or, if you're into Lua:

```lua
updateChatUserTyping={_='updateChatUserTyping', chat_id=int, user_id=int, action=SendMessageAction}

```


