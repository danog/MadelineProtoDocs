---
title: updateUserTyping
description: updateUserTyping attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: updateUserTyping  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|action|[SendMessageAction](../types/SendMessageAction.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```
$updateUserTyping = ['_' => 'updateUserTyping', 'user_id' => int, 'action' => SendMessageAction];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateUserTyping", "user_id": int, "action": SendMessageAction}
```


Or, if you're into Lua:  


```
updateUserTyping={_='updateUserTyping', user_id=int, action=SendMessageAction}

```


