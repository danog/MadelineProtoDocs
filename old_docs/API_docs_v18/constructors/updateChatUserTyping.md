---
title: updateChatUserTyping
description: updateChatUserTyping attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: updateChatUserTyping  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|
|user\_id|[int](../types/int.md) | Yes|
|action|[SendMessageAction](../types/SendMessageAction.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```
$updateChatUserTyping = ['_' => 'updateChatUserTyping', 'chat_id' => int, 'user_id' => int, 'action' => SendMessageAction];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChatUserTyping", "chat_id": int, "user_id": int, "action": SendMessageAction}
```


Or, if you're into Lua:  


```
updateChatUserTyping={_='updateChatUserTyping', chat_id=int, user_id=int, action=SendMessageAction}

```


