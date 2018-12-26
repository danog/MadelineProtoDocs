---
title: chatFull
description: Chat full
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatFull  
[Back to constructors index](index.md)



Chat full

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|participants|[ChatParticipants](../types/ChatParticipants.md) | Yes|Participants|
|chat\_photo|[Photo](../types/Photo.md) | Optional|Chat photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notify settings|



### Type: [ChatFull](../types/ChatFull.md)


### Example:

```php
$chatFull = ['_' => 'chatFull', 'id' => int, 'participants' => ChatParticipants, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatFull", "id": int, "participants": ChatParticipants, "chat_photo": Photo, "notify_settings": PeerNotifySettings}
```


Or, if you're into Lua:

```lua
chatFull={_='chatFull', id=int, participants=ChatParticipants, chat_photo=Photo, notify_settings=PeerNotifySettings}

```


