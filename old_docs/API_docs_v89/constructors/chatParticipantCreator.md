---
title: chatParticipantCreator
description: Chat participant creator
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatParticipantCreator  
[Back to constructors index](index.md)



Chat participant creator

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|



### Type: [ChatParticipant](../types/ChatParticipant.md)


### Example:

```php
$chatParticipantCreator = ['_' => 'chatParticipantCreator', 'user_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatParticipantCreator", "user_id": int}
```


Or, if you're into Lua:

```lua
chatParticipantCreator={_='chatParticipantCreator', user_id=int}

```


