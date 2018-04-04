---
title: chatParticipantsForbidden
description: chatParticipantsForbidden attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: chatParticipantsForbidden  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|



### Type: [ChatParticipants](../types/ChatParticipants.md)


### Example:

```
$chatParticipantsForbidden = ['_' => 'chatParticipantsForbidden', 'chat_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatParticipantsForbidden", "chat_id": int}
```


Or, if you're into Lua:  


```
chatParticipantsForbidden={_='chatParticipantsForbidden', chat_id=int}

```


