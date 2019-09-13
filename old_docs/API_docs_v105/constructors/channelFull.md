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
|hidden\_prehistory|[Bool](../types/Bool.md) | Optional|Hidden prehistory?|
|can\_view\_stats|[Bool](../types/Bool.md) | Optional|Can view stats?|
|can\_set\_location|[Bool](../types/Bool.md) | Optional|Can set location?|
|has\_scheduled|[Bool](../types/Bool.md) | Optional|Has scheduled messages?|
|id|[int](../types/int.md) | Yes|ID|
|about|[string](../types/string.md) | Yes|About|
|participants\_count|[int](../types/int.md) | Optional|Participants count|
|admins\_count|[int](../types/int.md) | Optional|Admins count|
|kicked\_count|[int](../types/int.md) | Optional|Kicked count|
|banned\_count|[int](../types/int.md) | Optional|Banned count|
|online\_count|[int](../types/int.md) | Optional|Online count|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Read inbox max ID|
|read\_outbox\_max\_id|[int](../types/int.md) | Yes|Read outbox max ID|
|unread\_count|[int](../types/int.md) | Yes|Unread count|
|chat\_photo|[Photo](../types/Photo.md) | Optional|Chat photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Yes|Notify settings|
|exported\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|Exported invite|
|bot\_info|Array of [BotInfo](../types/BotInfo.md) | Yes|Bot info|
|migrated\_from\_chat\_id|[int](../types/int.md) | Optional|Migrated from chat ID|
|migrated\_from\_max\_id|[int](../types/int.md) | Optional|Migrated from max ID|
|pinned\_msg\_id|[int](../types/int.md) | Optional|Pinned msg ID|
|stickerset|[StickerSet](../types/StickerSet.md) | Optional|Stickerset|
|available\_min\_id|[int](../types/int.md) | Optional|Available min ID|
|folder\_id|[int](../types/int.md) | Optional|Folder ID|
|linked\_chat\_id|[int](../types/int.md) | Optional|Linked chat ID|
|location|[ChannelLocation](../types/ChannelLocation.md) | Optional|Location|
|slowmode\_seconds|[int](../types/int.md) | Optional|If specified, users in supergroups will only be able to send one message every `slowmode_seconds` seconds|
|slowmode\_next\_send\_date|[int](../types/int.md) | Optional| Indicates when the user will be allowed to send another message in the supergroup (unixdate)|
|pts|[int](../types/int.md) | Yes|PTS|



### Type: [ChatFull](../types/ChatFull.md)


### Example:

```php
$channelFull = ['_' => 'channelFull', 'can_view_participants' => Bool, 'can_set_username' => Bool, 'can_set_stickers' => Bool, 'hidden_prehistory' => Bool, 'can_view_stats' => Bool, 'can_set_location' => Bool, 'has_scheduled' => Bool, 'id' => int, 'about' => 'string', 'participants_count' => int, 'admins_count' => int, 'kicked_count' => int, 'banned_count' => int, 'online_count' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'migrated_from_chat_id' => int, 'migrated_from_max_id' => int, 'pinned_msg_id' => int, 'stickerset' => StickerSet, 'available_min_id' => int, 'folder_id' => int, 'linked_chat_id' => int, 'location' => ChannelLocation, 'slowmode_seconds' => int, 'slowmode_next_send_date' => int, 'pts' => int];
```  


Or, if you're into Lua:

```lua
channelFull={_='channelFull', can_view_participants=Bool, can_set_username=Bool, can_set_stickers=Bool, hidden_prehistory=Bool, can_view_stats=Bool, can_set_location=Bool, has_scheduled=Bool, id=int, about='string', participants_count=int, admins_count=int, kicked_count=int, banned_count=int, online_count=int, read_inbox_max_id=int, read_outbox_max_id=int, unread_count=int, chat_photo=Photo, notify_settings=PeerNotifySettings, exported_invite=ExportedChatInvite, bot_info={BotInfo}, migrated_from_chat_id=int, migrated_from_max_id=int, pinned_msg_id=int, stickerset=StickerSet, available_min_id=int, folder_id=int, linked_chat_id=int, location=ChannelLocation, slowmode_seconds=int, slowmode_next_send_date=int, pts=int}

```


