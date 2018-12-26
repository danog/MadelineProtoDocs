---
title: channelFull
description: Full channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelFull  
[Back to constructors index](index.md)



Full channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_view\_participants|[Bool](../types/Bool.md) | Optional|Can view participants?|
|can\_set\_username|[Bool](../types/Bool.md) | Optional|Can set username?|
|can\_set\_stickers|[Bool](../types/Bool.md) | Optional|Can set group stickerset?|
|id|[int](../types/int.md) | Yes|ID|
|about|[string](../types/string.md) | Yes|About|
|participants\_count|[int](../types/int.md) | Optional|Participants count|
|admins\_count|[int](../types/int.md) | Optional|Admins count|
|kicked\_count|[int](../types/int.md) | Optional|Kicked count|
|banned\_count|[int](../types/int.md) | Optional|Banned count|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Read inbox max ID|
|read\_outbox\_max\_id|[int](../types/int.md) | Yes|Read outbox max ID|
|unread\_count|[int](../types/int.md) | Yes|Unread count|
|chat\_photo|[Photo](../types/Photo.md) | Optional|Chat photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notify settings|
|exported\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|Exported invite|
|bot\_info|Array of [BotInfo](../types/BotInfo.md) | Yes|Bot info|
|migrated\_from\_chat\_id|[int](../types/int.md) | Optional|Migrated from chat ID|
|migrated\_from\_max\_id|[int](../types/int.md) | Optional|Migrated from max ID|
|pinned\_msg\_id|[int](../types/int.md) | Optional|Pinned msg ID|
|stickerset|[StickerSet](../types/StickerSet.md) | Optional|Stickerset|



### Type: [ChatFull](../types/ChatFull.md)


### Example:

```php
$channelFull = ['_' => 'channelFull', 'can_view_participants' => Bool, 'can_set_username' => Bool, 'can_set_stickers' => Bool, 'id' => int, 'about' => 'string', 'participants_count' => int, 'admins_count' => int, 'kicked_count' => int, 'banned_count' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'migrated_from_chat_id' => int, 'migrated_from_max_id' => int, 'pinned_msg_id' => int, 'stickerset' => StickerSet];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelFull", "can_view_participants": Bool, "can_set_username": Bool, "can_set_stickers": Bool, "id": int, "about": "string", "participants_count": int, "admins_count": int, "kicked_count": int, "banned_count": int, "read_inbox_max_id": int, "read_outbox_max_id": int, "unread_count": int, "chat_photo": Photo, "notify_settings": PeerNotifySettings, "exported_invite": ExportedChatInvite, "bot_info": [BotInfo], "migrated_from_chat_id": int, "migrated_from_max_id": int, "pinned_msg_id": int, "stickerset": StickerSet}
```


Or, if you're into Lua:

```lua
channelFull={_='channelFull', can_view_participants=Bool, can_set_username=Bool, can_set_stickers=Bool, id=int, about='string', participants_count=int, admins_count=int, kicked_count=int, banned_count=int, read_inbox_max_id=int, read_outbox_max_id=int, unread_count=int, chat_photo=Photo, notify_settings=PeerNotifySettings, exported_invite=ExportedChatInvite, bot_info={BotInfo}, migrated_from_chat_id=int, migrated_from_max_id=int, pinned_msg_id=int, stickerset=StickerSet}

```


