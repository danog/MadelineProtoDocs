---
title: chatFull
description: Detailed chat info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatFull  
[Back to constructors index](index.md)



Detailed chat info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_set\_username|[Bool](../types/Bool.md) | Optional|Can we change the username of this chat|
|id|[int](../types/int.md) | Yes|ID of the chat|
|about|[string](../types/string.md) | Yes|About string for this chat|
|participants|[ChatParticipants](../types/ChatParticipants.md) | Yes|Participant list|
|chat\_photo|[Photo](../types/Photo.md) | Optional|Chat photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Yes|Notification settings|
|exported\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|Chat invite|
|bot\_info|Array of [BotInfo](../types/BotInfo.md) | Optional|Info about bots that are in this chat|
|pinned\_msg\_id|[int](../types/int.md) | Optional|Message ID of the last [pinned message](https://core.telegram.org/api/pin)|



### Type: [ChatFull](../types/ChatFull.md)


### Example:

```php
$chatFull = ['_' => 'chatFull', 'can_set_username' => Bool, 'id' => int, 'about' => 'string', 'participants' => ChatParticipants, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'pinned_msg_id' => int];
```  


Or, if you're into Lua:

```lua
chatFull={_='chatFull', can_set_username=Bool, id=int, about='string', participants=ChatParticipants, chat_photo=Photo, notify_settings=PeerNotifySettings, exported_invite=ExportedChatInvite, bot_info={BotInfo}, pinned_msg_id=int}

```


