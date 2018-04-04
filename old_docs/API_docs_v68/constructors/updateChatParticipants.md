---
title: updateChatParticipants
description: updateChatParticipants attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: updateChatParticipants  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|participants|[ChatParticipants](../types/ChatParticipants.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```
$updateChatParticipants = ['_' => 'updateChatParticipants', 'participants' => ChatParticipants];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChatParticipants", "participants": ChatParticipants}
```


Or, if you're into Lua:  


```
updateChatParticipants={_='updateChatParticipants', participants=ChatParticipants}

```


