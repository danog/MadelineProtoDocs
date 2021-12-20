---
title: "channelFull"
description: "Full info about a channel/supergroup"
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
|hidden\_prehistory|[Bool](../types/Bool.md) | Optional|Is the history before we joined hidden to us?|
|can\_set\_location|[Bool](../types/Bool.md) | Optional|Can we set the geolocation of this group (for geogroups)|
|has\_scheduled|[Bool](../types/Bool.md) | Optional|Whether scheduled messages are available|
|can\_view\_stats|[Bool](../types/Bool.md) | Optional|Can the user view [channel/supergroup statistics](https://core.telegram.org/api/stats)|
|blocked|[Bool](../types/Bool.md) | Optional|Whether any anonymous admin of this supergroup was blocked: if set, you won't receive messages from anonymous group admins in [discussion replies via @replies](https://core.telegram.org/api/discussion)|
|id|[long](../types/long.md) | Yes|
|about|[string](../types/string.md) | Yes|Info about the channel|
|participants\_count|[int](../types/int.md) | Optional|Number of participants of the channel|
|admins\_count|[int](../types/int.md) | Optional|Number of channel admins|
|kicked\_count|[int](../types/int.md) | Optional|Number of users [kicked](https://core.telegram.org/api/rights) from the channel|
|banned\_count|[int](../types/int.md) | Optional|Number of users [banned](https://core.telegram.org/api/rights) from the channel|
|online\_count|[int](../types/int.md) | Optional|Number of users currently online|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Position up to which all incoming messages are read.|
|read\_outbox\_max\_id|[int](../types/int.md) | Yes|Position up to which all outgoing messages are read.|
|unread\_count|[int](../types/int.md) | Yes|Count of unread messages|
|chat\_photo|[Photo](../types/Photo.md) | Optional|Channel picture|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Yes|Notification settings|
|exported\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Optional|Invite link|
|bot\_info|Array of [BotInfo](../types/BotInfo.md) | Yes|Info about bots in the channel/supergrup|
|migrated\_from\_chat\_id|[long](../types/long.md) | Optional|
|migrated\_from\_max\_id|[int](../types/int.md) | Optional|The message ID in the original chat at which this group was [migrated](https://core.telegram.org/api/channel)|
|pinned\_msg\_id|[int](../types/int.md) | Optional|Message ID of the last [pinned message](https://core.telegram.org/api/pin)|
|stickerset|[StickerSet](../types/StickerSet.md) | Optional|Associated stickerset|
|available\_min\_id|[int](../types/int.md) | Optional|Identifier of a maximum unavailable message in a channel due to hidden history.|
|folder\_id|[int](../types/int.md) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|linked\_chat\_id|[long](../types/long.md) | Optional|
|location|[ChannelLocation](../types/ChannelLocation.md) | Optional|Location of the geogroup|
|slowmode\_seconds|[int](../types/int.md) | Optional|If specified, users in supergroups will only be able to send one message every `slowmode_seconds` seconds|
|slowmode\_next\_send\_date|[int](../types/int.md) | Optional|Indicates when the user will be allowed to send another message in the supergroup (unixdate)|
|stats\_dc|[int](../types/int.md) | Optional|If set, specifies the DC to use for fetching channel statistics|
|pts|[int](../types/int.md) | Yes|Latest [PTS](https://core.telegram.org/api/updates) for this channel|
|call|[InputGroupCall](../types/InputGroupCall.md) | Optional|
|ttl\_period|[int](../types/int.md) | Optional|
|pending\_suggestions|Array of [string](../types/string.md) | Optional|
|groupcall\_default\_join\_as|[Peer](../types/Peer.md) | Optional|
|theme\_emoticon|[string](../types/string.md) | Optional|
|requests\_pending|[int](../types/int.md) | Optional|
|recent\_requesters|Array of [long](../types/long.md) | Optional|
|default\_send\_as|[Peer](../types/Peer.md) | Optional|



### Type: [ChatFull](../types/ChatFull.md)


### Example:

```php
$channelFull = ['_' => 'channelFull', 'can_view_participants' => Bool, 'can_set_username' => Bool, 'can_set_stickers' => Bool, 'hidden_prehistory' => Bool, 'can_set_location' => Bool, 'has_scheduled' => Bool, 'can_view_stats' => Bool, 'blocked' => Bool, 'id' => long, 'about' => 'string', 'participants_count' => int, 'admins_count' => int, 'kicked_count' => int, 'banned_count' => int, 'online_count' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'migrated_from_chat_id' => long, 'migrated_from_max_id' => int, 'pinned_msg_id' => int, 'stickerset' => StickerSet, 'available_min_id' => int, 'folder_id' => int, 'linked_chat_id' => long, 'location' => ChannelLocation, 'slowmode_seconds' => int, 'slowmode_next_send_date' => int, 'stats_dc' => int, 'pts' => int, 'call' => InputGroupCall, 'ttl_period' => int, 'pending_suggestions' => ['string', 'string'], 'groupcall_default_join_as' => Peer, 'theme_emoticon' => 'string', 'requests_pending' => int, 'recent_requesters' => [long, long], 'default_send_as' => Peer];
```  


Or, if you're into Lua:

```lua
channelFull={_='channelFull', can_view_participants=Bool, can_set_username=Bool, can_set_stickers=Bool, hidden_prehistory=Bool, can_set_location=Bool, has_scheduled=Bool, can_view_stats=Bool, blocked=Bool, id=long, about='string', participants_count=int, admins_count=int, kicked_count=int, banned_count=int, online_count=int, read_inbox_max_id=int, read_outbox_max_id=int, unread_count=int, chat_photo=Photo, notify_settings=PeerNotifySettings, exported_invite=ExportedChatInvite, bot_info={BotInfo}, migrated_from_chat_id=long, migrated_from_max_id=int, pinned_msg_id=int, stickerset=StickerSet, available_min_id=int, folder_id=int, linked_chat_id=long, location=ChannelLocation, slowmode_seconds=int, slowmode_next_send_date=int, stats_dc=int, pts=int, call=InputGroupCall, ttl_period=int, pending_suggestions={'string'}, groupcall_default_join_as=Peer, theme_emoticon='string', requests_pending=int, recent_requesters={long}, default_send_as=Peer}

```


