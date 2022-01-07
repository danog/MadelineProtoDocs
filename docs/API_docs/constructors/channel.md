---
title: "channel"
description: "Channel/supergroup info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channel  
[Back to constructors index](/API_docs/constructors/index.md)



Channel/supergroup info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](/API_docs/types/Bool.md) | Optional|Whether the current user is the creator of this channel|
|left|[Bool](/API_docs/types/Bool.md) | Optional|Whether the current user has left this channel|
|broadcast|[Bool](/API_docs/types/Bool.md) | Optional|Is this a channel?|
|verified|[Bool](/API_docs/types/Bool.md) | Optional|Is this channel verified by telegram?|
|megagroup|[Bool](/API_docs/types/Bool.md) | Optional|Is this a supergroup?|
|restricted|[Bool](/API_docs/types/Bool.md) | Optional|Whether viewing/writing in this channel for a reason (see `restriction_reason`|
|signatures|[Bool](/API_docs/types/Bool.md) | Optional|Whether signatures are enabled (channels)|
|min|[Bool](/API_docs/types/Bool.md) | Optional|See [min](https://core.telegram.org/api/min)|
|scam|[Bool](/API_docs/types/Bool.md) | Optional|This channel/supergroup is probably a scam|
|has\_link|[Bool](/API_docs/types/Bool.md) | Optional|Whether this channel has a private join link|
|has\_geo|[Bool](/API_docs/types/Bool.md) | Optional|Whether this chanel has a geoposition|
|slowmode\_enabled|[Bool](/API_docs/types/Bool.md) | Optional|Whether slow mode is enabled for groups to prevent flood in chat|
|call\_active|[Bool](/API_docs/types/Bool.md) | Optional|
|call\_not\_empty|[Bool](/API_docs/types/Bool.md) | Optional|
|fake|[Bool](/API_docs/types/Bool.md) | Optional|
|gigagroup|[Bool](/API_docs/types/Bool.md) | Optional|
|noforwards|[Bool](/API_docs/types/Bool.md) | Optional|
|id|[long](/API_docs/types/long.md) | Yes|
|access\_hash|[long](/API_docs/types/long.md) | Optional|Access hash|
|title|[string](/API_docs/types/string.md) | Yes|Title|
|username|[string](/API_docs/types/string.md) | Optional|Username|
|photo|[ChatPhoto](/API_docs/types/ChatPhoto.md) | Optional|Profile photo|
|date|[int](/API_docs/types/int.md) | Yes|Date when the user joined the supergroup/channel, or if the user isn't a member, its creation date|
|restriction\_reason|Array of [RestrictionReason](/API_docs/types/RestrictionReason.md) | Optional|Contains the reason why access to this channel must be restricted.|
|admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.md) | Optional|Admin rights of the user in this channel (see [rights](https://core.telegram.org/api/rights))|
|banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.md) | Optional|Banned rights of the user in this channel (see [rights](https://core.telegram.org/api/rights))|
|default\_banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.md) | Optional|Default chat rights (see [rights](https://core.telegram.org/api/rights))|
|participants\_count|[int](/API_docs/types/int.md) | Optional|Participant count|



### Type: [Chat](/API_docs/types/Chat.md)


### Example:

```php
$channel = ['_' => 'channel', 'creator' => Bool, 'left' => Bool, 'broadcast' => Bool, 'verified' => Bool, 'megagroup' => Bool, 'restricted' => Bool, 'signatures' => Bool, 'min' => Bool, 'scam' => Bool, 'has_link' => Bool, 'has_geo' => Bool, 'slowmode_enabled' => Bool, 'call_active' => Bool, 'call_not_empty' => Bool, 'fake' => Bool, 'gigagroup' => Bool, 'noforwards' => Bool, 'id' => long, 'access_hash' => long, 'title' => 'string', 'username' => 'string', 'photo' => ChatPhoto, 'date' => int, 'restriction_reason' => [RestrictionReason, RestrictionReason], 'admin_rights' => ChatAdminRights, 'banned_rights' => ChatBannedRights, 'default_banned_rights' => ChatBannedRights, 'participants_count' => int];
```  
