---
title: chatParticipantCreator
description: chatParticipantCreator attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantCreator  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|



### Type: [ChatParticipant](../types/ChatParticipant.md)


### Example:

```
$chatParticipantCreator = ['_' => 'chatParticipantCreator', 'user_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatParticipantCreator", "user_id": int}
```


Or, if you're into Lua:  


```
chatParticipantCreator={_='chatParticipantCreator', user_id=int}

```


