---
title: "channel"
description: "Channel/supergroup info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channel  
[Back to constructors index](/API_docs/constructors/index.html)



Channel/supergroup info

When updating the [local peer database](https://core.telegram.org/api/peers), all fields from the newly received constructor take priority over the old constructor cached locally (including by removing fields that aren't set in the new constructor).

The only exception to the above rule is when the `min` flag is set, in which case **only** the following fields must be applied over any locally stored version:

- `title`
- `megagroup`
- `color`
- `photo`
- `username`
- `usernames`
- `has_geo`
- `noforwards`
- `emoji_status`
- `has_link`
- `slow_mode_enabled`
- `scam`
- `fake`
- `gigagroup`
- `forum`
- `level`
- `restricted`
- `restriction_reason`
- `join_to_send`
- `join_request`
- `is_verified`
- `default_banned_rights`
- `signature_profiles`

See [here »](https://github.com/tdlib/td/blob/a24af0992245f838f2b4b418a0a2d5fa9caa27b5/td/telegram/ChatManager.cpp#L8329) for an implementation of the logic to use when updating the [local user peer database](https://core.telegram.org/api/peers).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|Whether the current user is the creator of this channel|
|left|[Bool](/API_docs/types/Bool.html) | Optional|Whether the current user has left or is not a member of this channel|
|broadcast|[Bool](/API_docs/types/Bool.html) | Optional|Is this a channel?|
|verified|[Bool](/API_docs/types/Bool.html) | Optional|Is this channel verified by telegram?|
|megagroup|[Bool](/API_docs/types/Bool.html) | Optional|Is this a supergroup? <br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|restricted|[Bool](/API_docs/types/Bool.html) | Optional|Whether viewing/writing in this channel for a reason (see `restriction_reason`)|
|signatures|[Bool](/API_docs/types/Bool.html) | Optional|Whether signatures are enabled (channels)|
|min|[Bool](/API_docs/types/Bool.html) | Optional|See [min](https://core.telegram.org/api/min)|
|scam|[Bool](/API_docs/types/Bool.html) | Optional|This channel/supergroup is probably a scam <br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|has\_link|[Bool](/API_docs/types/Bool.html) | Optional|Whether this channel has a linked [discussion group »](https://core.telegram.org/api/discussion) (or this supergroup is a channel's discussion group). The actual ID of the linked channel/supergroup is contained in [channelFull](../constructors/channelFull.html).`linked_chat_id`. <br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|has\_geo|[Bool](/API_docs/types/Bool.html) | Optional|Whether this chanel has a geoposition|
|slowmode\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|Whether slow mode is enabled for groups to prevent flood in chat. <br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|call\_active|[Bool](/API_docs/types/Bool.html) | Optional|Whether a group call or livestream is currently active|
|call\_not\_empty|[Bool](/API_docs/types/Bool.html) | Optional|Whether there's anyone in the group call or livestream|
|fake|[Bool](/API_docs/types/Bool.html) | Optional|If set, this [supergroup/channel](https://core.telegram.org/api/channel) was reported by many users as a fake or scam: be careful when interacting with it. <br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|gigagroup|[Bool](/API_docs/types/Bool.html) | Optional|Whether this [supergroup](https://core.telegram.org/api/channel) is a gigagroup<br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|noforwards|[Bool](/API_docs/types/Bool.html) | Optional|Whether this channel or group is [protected](https://telegram.org/blog/protected-content-delete-by-date-and-more), thus does not allow forwarding messages from it|
|join\_to\_send|[Bool](/API_docs/types/Bool.html) | Optional|Whether a user needs to join the supergroup before they can send messages: can be false only for [discussion groups »](https://core.telegram.org/api/discussion), toggle using [channels.toggleJoinToSend](../methods/channels.toggleJoinToSend.html)<br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|join\_request|[Bool](/API_docs/types/Bool.html) | Optional|Whether a user's join request will have to be [approved by administrators](https://core.telegram.org/api/invites#join-requests), toggle using [channels.toggleJoinToSend](../methods/channels.toggleJoinRequest.html)<br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|forum|[Bool](/API_docs/types/Bool.html) | Optional|Whether this supergroup is a [forum](https://core.telegram.org/api/forum). <br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|stories\_hidden|[Bool](/API_docs/types/Bool.html) | Optional|
|stories\_hidden\_min|[Bool](/API_docs/types/Bool.html) | Optional|
|stories\_unavailable|[Bool](/API_docs/types/Bool.html) | Optional|
|signature\_profiles|[Bool](/API_docs/types/Bool.html) | Optional|
|autotranslation|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|ID of the channel, see [here »](https://core.telegram.org/api/peers#peer-id) for more info|
|access\_hash|[long](/API_docs/types/long.html) | Optional|Access hash, see [here »](https://core.telegram.org/api/peers#access-hash) for more info|
|title|[string](/API_docs/types/string.html) | Yes|Title|
|username|[string](/API_docs/types/string.html) | Optional|Main active username.|
|photo|[ChatPhoto](/API_docs/types/ChatPhoto.html) | Optional|Profile photo|
|date|[int](/API_docs/types/int.html) | Yes|Date when the user joined the supergroup/channel, or if the user isn't a member, its creation date|
|restriction\_reason|Array of [RestrictionReason](/API_docs/types/RestrictionReason.html) | Optional|Contains the reason why access to this channel must be restricted. <br>Changes to this flag should invalidate the local [channelFull](../constructors/channelFull.html) cache for this channel/supergroup ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Optional|Admin rights of the user in this channel (see [rights](https://core.telegram.org/api/rights))|
|banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.html) | Optional|Banned rights of the user in this channel (see [rights](https://core.telegram.org/api/rights))|
|default\_banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.html) | Optional|Default chat rights (see [rights](https://core.telegram.org/api/rights))|
|participants\_count|[int](/API_docs/types/int.html) | Optional|Participant count|
|usernames|Array of [Username](/API_docs/types/Username.html) | Optional|
|stories\_max\_id|[int](/API_docs/types/int.html) | Optional|
|color|[PeerColor](/API_docs/types/PeerColor.html) | Optional|
|profile\_color|[PeerColor](/API_docs/types/PeerColor.html) | Optional|
|emoji\_status|[EmojiStatus](/API_docs/types/EmojiStatus.html) | Optional|
|level|[int](/API_docs/types/int.html) | Optional|
|subscription\_until\_date|[int](/API_docs/types/int.html) | Optional|
|bot\_verification\_icon|[long](/API_docs/types/long.html) | Optional|
|send\_paid\_messages\_stars|[long](/API_docs/types/long.html) | Optional|



### Type: [Chat](/API_docs/types/Chat.html)


### Example:

```
$channel = ['_' => 'channel', 'creator' => Bool, 'left' => Bool, 'broadcast' => Bool, 'verified' => Bool, 'megagroup' => Bool, 'restricted' => Bool, 'signatures' => Bool, 'min' => Bool, 'scam' => Bool, 'has_link' => Bool, 'has_geo' => Bool, 'slowmode_enabled' => Bool, 'call_active' => Bool, 'call_not_empty' => Bool, 'fake' => Bool, 'gigagroup' => Bool, 'noforwards' => Bool, 'join_to_send' => Bool, 'join_request' => Bool, 'forum' => Bool, 'stories_hidden' => Bool, 'stories_hidden_min' => Bool, 'stories_unavailable' => Bool, 'signature_profiles' => Bool, 'autotranslation' => Bool, 'id' => long, 'access_hash' => long, 'title' => 'string', 'username' => 'string', 'photo' => ChatPhoto, 'date' => int, 'restriction_reason' => [RestrictionReason, RestrictionReason], 'admin_rights' => ChatAdminRights, 'banned_rights' => ChatBannedRights, 'default_banned_rights' => ChatBannedRights, 'participants_count' => int, 'usernames' => [Username, Username], 'stories_max_id' => int, 'color' => PeerColor, 'profile_color' => PeerColor, 'emoji_status' => EmojiStatus, 'level' => int, 'subscription_until_date' => int, 'bot_verification_icon' => long, 'send_paid_messages_stars' => long];
```  
