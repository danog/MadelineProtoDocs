---
title: channelFull
description: Full info about a [channel/supergroup](https://core.telegram.org/api/channel)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelFull  
[Back to constructors index](index.md)



Full info about a [channel/supergroup](https://core.telegram.org/api/channel)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_view\_participants|[Bool](../types/Bool.md) | Optional|Can we vew the participant list?|
|can\_set\_username|[Bool](../types/Bool.md) | Optional|Can we set the channel's username?|
|can\_set\_stickers|[Bool](../types/Bool.md) | Optional|Can we [associate](../methods/channels.setStickers.md) a stickerpack to the supergroup?|
|id|[int](../types/int.md) | Yes|ID of the channel|
|about|[string](../types/string.md) | Yes|Info about the channel|
|participants\_count|[int](../types/int.md) | Optional|Number of participants of the channel|
|admins\_count|[int](../types/int.md) | Optional|Number of channel admins|
|kicked\_count|[int](../types/int.md) | Optional|Number of users [kicked](https://core.telegram.org/api/rights) from the channel|
|banned\_count|[int](../types/int.md) | Optional|Number of users [banned](https://core.telegram.org/api/rights) from the channel|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Position up to which all incoming messages are read.|
|read\_outbox\_max\_id|[int](../types/int.md) | Yes|Position up to which all outgoing messages are read.|
|unread\_count|[int](../types/int.md) | Yes|Count of unread messages|
|chat\_photo|[Photo](../types/Photo.md) | Optional|Channel picture|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notification settings|
|exported\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|Invite link|
|bot\_info|Array of [BotInfo](../types/BotInfo.md) | Yes|Info about bots in the channel/supergrup|
|migrated\_from\_chat\_id|[int](../types/int.md) | Optional|The chat ID from which this group was [migrated](https://core.telegram.org/api/channel)|
|migrated\_from\_max\_id|[int](../types/int.md) | Optional|The message ID in the original chat at which this group was [migrated](https://core.telegram.org/api/channel)|
|pinned\_msg\_id|[int](../types/int.md) | Optional|Message ID of the last [pinned message](https://core.telegram.org/api/pin)|
|stickerset|[StickerSet](../types/StickerSet.md) | Optional|Associated stickerset|



### Type: [ChatFull](../types/ChatFull.md)


### Example:

```php
$channelFull = ['_' => 'channelFull', 'can_view_participants' => Bool, 'can_set_username' => Bool, 'can_set_stickers' => Bool, 'id' => int, 'about' => 'string', 'participants_count' => int, 'admins_count' => int, 'kicked_count' => int, 'banned_count' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'migrated_from_chat_id' => int, 'migrated_from_max_id' => int, 'pinned_msg_id' => int, 'stickerset' => StickerSet];
```  


Or, if you're into Lua:

```lua
channelFull={_='channelFull', can_view_participants=Bool, can_set_username=Bool, can_set_stickers=Bool, id=int, about='string', participants_count=int, admins_count=int, kicked_count=int, banned_count=int, read_inbox_max_id=int, read_outbox_max_id=int, unread_count=int, chat_photo=Photo, notify_settings=PeerNotifySettings, exported_invite=ExportedChatInvite, bot_info={BotInfo}, migrated_from_chat_id=int, migrated_from_max_id=int, pinned_msg_id=int, stickerset=StickerSet}

```


