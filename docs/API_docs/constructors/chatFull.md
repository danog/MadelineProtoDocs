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
|can\_set\_username|[Bool](../types/Bool.md) | Optional|Can set username?|
|id|[int](../types/int.md) | Yes|ID|
|about|[string](../types/string.md) | Yes|Chat about|
|participants|[ChatParticipants](../types/ChatParticipants.md) | Yes|Participants|
|chat\_photo|[Photo](../types/Photo.md) | Optional|Chat photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Yes|Notify settings|
|exported\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|Exported invite|
|bot\_info|Array of [BotInfo](../types/BotInfo.md) | Optional|Bot info|
|pinned\_msg\_id|[int](../types/int.md) | Optional|Pinned msg ID|



### Type: [ChatFull](../types/ChatFull.md)


### Example:

```php
$chatFull = ['_' => 'chatFull', 'can_set_username' => Bool, 'id' => int, 'about' => 'string', 'participants' => ChatParticipants, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'pinned_msg_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatFull", "can_set_username": Bool, "id": int, "about": "string", "participants": ChatParticipants, "chat_photo": Photo, "notify_settings": PeerNotifySettings, "exported_invite": ExportedChatInvite, "bot_info": [BotInfo], "pinned_msg_id": int}
```


Or, if you're into Lua:

```lua
chatFull={_='chatFull', can_set_username=Bool, id=int, about='string', participants=ChatParticipants, chat_photo=Photo, notify_settings=PeerNotifySettings, exported_invite=ExportedChatInvite, bot_info={BotInfo}, pinned_msg_id=int}

```


