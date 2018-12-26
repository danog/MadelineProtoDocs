---
title: chatParticipantsForbidden
description: Chat participants forbidden
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantsForbidden  
[Back to constructors index](index.md)



Chat participants forbidden

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|



### Type: [ChatParticipants](../types/ChatParticipants.md)


### Example:

```php
$chatParticipantsForbidden = ['_' => 'chatParticipantsForbidden', 'chat_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatParticipantsForbidden", "chat_id": int}
```


Or, if you're into Lua:

```lua
chatParticipantsForbidden={_='chatParticipantsForbidden', chat_id=int}

```


