---
title: "channelFull"
description: "Full info about a channel, supergroup or gigagroup."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelFull  
[Back to constructors index](/API_docs/constructors/index.html)



Full info about a [channel](https://core.telegram.org/api/channel#channels), [supergroup](https://core.telegram.org/api/channel#supergroups) or [gigagroup](https://core.telegram.org/api/channel#gigagroups).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_view\_participants|[Bool](/API_docs/types/Bool.html) | Optional|Can we view the participant list?|
|can\_set\_username|[Bool](/API_docs/types/Bool.html) | Optional|Can we set the channel's username?|
|can\_set\_stickers|[Bool](/API_docs/types/Bool.html) | Optional|Can we [associate](../methods/channels.setStickers.html) a stickerpack to the supergroup?|
|hidden\_prehistory|[Bool](/API_docs/types/Bool.html) | Optional|Is the history before we joined hidden to us?|
|can\_set\_location|[Bool](/API_docs/types/Bool.html) | Optional|Can we set the geolocation of this group (for geogroups)|
|has\_scheduled|[Bool](/API_docs/types/Bool.html) | Optional|Whether scheduled messages are available|
|can\_view\_stats|[Bool](/API_docs/types/Bool.html) | Optional|Can the user view [channel/supergroup statistics](https://core.telegram.org/api/stats)|
|blocked|[Bool](/API_docs/types/Bool.html) | Optional|Whether any anonymous admin of this supergroup was blocked: if set, you won't receive messages from anonymous group admins in [discussion replies via @replies](https://core.telegram.org/api/discussion)|
|can\_delete\_channel|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|ID of the channel|
|about|[string](/API_docs/types/string.html) | Yes|Info about the channel|
|participants\_count|[int](/API_docs/types/int.html) | Optional|Number of participants of the channel|
|admins\_count|[int](/API_docs/types/int.html) | Optional|Number of channel admins|
|kicked\_count|[int](/API_docs/types/int.html) | Optional|Number of users [kicked](https://core.telegram.org/api/rights) from the channel|
|banned\_count|[int](/API_docs/types/int.html) | Optional|Number of users [banned](https://core.telegram.org/api/rights) from the channel|
|online\_count|[int](/API_docs/types/int.html) | Optional|Number of users currently online|
|read\_inbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all incoming messages are read.|
|read\_outbox\_max\_id|[int](/API_docs/types/int.html) | Yes|Position up to which all outgoing messages are read.|
|unread\_count|[int](/API_docs/types/int.html) | Yes|Count of unread messages|
|chat\_photo|[Photo](/API_docs/types/Photo.html) | Optional|Channel picture|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.html) | Yes|Notification settings|
|exported\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Optional|Invite link|
|bot\_info|Array of [BotInfo](/API_docs/types/BotInfo.html) | Yes|Info about bots in the channel/supergroup|
|migrated\_from\_chat\_id|[long](/API_docs/types/long.html) | Optional|The chat ID from which this group was [migrated](https://core.telegram.org/api/channel)|
|migrated\_from\_max\_id|[int](/API_docs/types/int.html) | Optional|The message ID in the original chat at which this group was [migrated](https://core.telegram.org/api/channel)|
|pinned\_msg\_id|[int](/API_docs/types/int.html) | Optional|Message ID of the last [pinned message](https://core.telegram.org/api/pin)|
|stickerset|[StickerSet](/API_docs/types/StickerSet.html) | Optional|Associated stickerset|
|available\_min\_id|[int](/API_docs/types/int.html) | Optional|Identifier of a maximum unavailable message in a channel due to hidden history.|
|folder\_id|[int](/API_docs/types/int.html) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|linked\_chat\_id|[long](/API_docs/types/long.html) | Optional|ID of the linked [discussion chat](https://core.telegram.org/api/discussion) for channels|
|location|[ChannelLocation](/API_docs/types/ChannelLocation.html) | Optional|Location of the geogroup|
|slowmode\_seconds|[int](/API_docs/types/int.html) | Optional|If specified, users in supergroups will only be able to send one message every `slowmode_seconds` seconds|
|slowmode\_next\_send\_date|[int](/API_docs/types/int.html) | Optional|Indicates when the user will be allowed to send another message in the supergroup (unixtime)|
|stats\_dc|[int](/API_docs/types/int.html) | Optional|If set, specifies the DC to use for fetching channel statistics|
|pts|[int](/API_docs/types/int.html) | Yes|Latest [PTS](https://core.telegram.org/api/updates) for this channel|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Optional|Livestream or group call information|
|ttl\_period|[int](/API_docs/types/int.html) | Optional|Time-To-Live of messages in this channel or supergroup|
|pending\_suggestions|Array of [string](/API_docs/types/string.html) | Optional|A list of [suggested actions](https://core.telegram.org/api/config#suggestions) for the supergroup admin, [see here for more info »](https://core.telegram.org/api/config#suggestions).|
|groupcall\_default\_join\_as|[Peer](/API_docs/types/Peer.html) | Optional|When using [phone.getGroupCallJoinAs](../methods/phone.getGroupCallJoinAs.html) to get a list of peers that can be used to join a group call, this field indicates the peer that should be selected by default.|
|theme\_emoticon|[string](/API_docs/types/string.html) | Optional|Emoji representing a specific chat theme|
|requests\_pending|[int](/API_docs/types/int.html) | Optional|Pending [join requests »](https://core.telegram.org/api/invites#join-requests)|
|recent\_requesters|Array of [long](/API_docs/types/long.html) | Optional|IDs of users who requested to join recently|
|default\_send\_as|[Peer](/API_docs/types/Peer.html) | Optional|Default peer used for sending messages to this channel|
|available\_reactions|Array of [string](/API_docs/types/string.html) | Optional|Allowed [message reactions »](https://core.telegram.org/api/reactions)|



### Type: [ChatFull](/API_docs/types/ChatFull.html)


### Example:

```
$channelFull = ['_' => 'channelFull', 'can_view_participants' => Bool, 'can_set_username' => Bool, 'can_set_stickers' => Bool, 'hidden_prehistory' => Bool, 'can_set_location' => Bool, 'has_scheduled' => Bool, 'can_view_stats' => Bool, 'blocked' => Bool, 'can_delete_channel' => Bool, 'id' => long, 'about' => 'string', 'participants_count' => int, 'admins_count' => int, 'kicked_count' => int, 'banned_count' => int, 'online_count' => int, 'read_inbox_max_id' => int, 'read_outbox_max_id' => int, 'unread_count' => int, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'migrated_from_chat_id' => long, 'migrated_from_max_id' => int, 'pinned_msg_id' => int, 'stickerset' => StickerSet, 'available_min_id' => int, 'folder_id' => int, 'linked_chat_id' => long, 'location' => ChannelLocation, 'slowmode_seconds' => int, 'slowmode_next_send_date' => int, 'stats_dc' => int, 'pts' => int, 'call' => InputGroupCall, 'ttl_period' => int, 'pending_suggestions' => ['string', 'string'], 'groupcall_default_join_as' => Peer, 'theme_emoticon' => 'string', 'requests_pending' => int, 'recent_requesters' => [long, long], 'default_send_as' => Peer, 'available_reactions' => ['string', 'string']];
```  
