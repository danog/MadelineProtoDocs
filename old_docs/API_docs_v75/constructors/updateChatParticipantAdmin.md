---
title: updateChatParticipantAdmin
description: updateChatParticipantAdmin attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChatParticipantAdmin  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|
|user\_id|[int](../types/int.md) | Yes|
|is\_admin|[Bool](../types/Bool.md) | Yes|
|version|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```
$updateChatParticipantAdmin = ['_' => 'updateChatParticipantAdmin', 'chat_id' => int, 'user_id' => int, 'is_admin' => Bool, 'version' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateChatParticipantAdmin", "chat_id": int, "user_id": int, "is_admin": Bool, "version": int}
```


Or, if you're into Lua:  


```
updateChatParticipantAdmin={_='updateChatParticipantAdmin', chat_id=int, user_id=int, is_admin=Bool, version=int}

```


