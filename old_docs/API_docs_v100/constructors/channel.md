---
title: channel
description: Channel/supergroup info
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channel  
[Back to constructors index](index.md)



Channel/supergroup info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](../types/Bool.md) | Optional|Whether the current user is the creator of this channel|
|left|[Bool](../types/Bool.md) | Optional|Whether the current user has left this channel|
|broadcast|[Bool](../types/Bool.md) | Optional|Is this a channel?|
|verified|[Bool](../types/Bool.md) | Optional|Is this channel verified by telegram?|
|megagroup|[Bool](../types/Bool.md) | Optional|Is this a supergroup?|
|restricted|[Bool](../types/Bool.md) | Optional|Whether viewing/writing in this channel for a reason (see `restriction_reason`|
|signatures|[Bool](../types/Bool.md) | Optional|Whether signatures are enabled (channels)|
|min|[Bool](../types/Bool.md) | Optional|See [min](https://core.telegram.org/api/min)|
|scam|[Bool](../types/Bool.md) | Optional|This channel/supergroup is probably a scam|
|has\_link|[Bool](../types/Bool.md) | Optional|Whether this channel has a private join link|
|id|[int](../types/int.md) | Yes|ID of the channel|
|access\_hash|[long](../types/long.md) | Optional|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|username|[string](../types/string.md) | Optional|Username|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Profile photo|
|date|[int](../types/int.md) | Yes|Creation date|
|version|[int](../types/int.md) | Yes|Version of the channel (always `0`)|
|restriction\_reason|[string](../types/string.md) | Optional|Restriction reason|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | Optional|Admin rights of the user in this channel (see [rights](https://core.telegram.org/api/rights))|
|banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Optional|Banned rights of the user in this channel (see [rights](https://core.telegram.org/api/rights))|
|default\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Optional|Default chat rights (see [rights](https://core.telegram.org/api/rights))|
|participants\_count|[int](../types/int.md) | Optional|Participant count|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$channel = ['_' => 'channel', 'creator' => Bool, 'left' => Bool, 'broadcast' => Bool, 'verified' => Bool, 'megagroup' => Bool, 'restricted' => Bool, 'signatures' => Bool, 'min' => Bool, 'scam' => Bool, 'has_link' => Bool, 'id' => int, 'access_hash' => long, 'title' => 'string', 'username' => 'string', 'photo' => ChatPhoto, 'date' => int, 'version' => int, 'restriction_reason' => 'string', 'admin_rights' => ChatAdminRights, 'banned_rights' => ChatBannedRights, 'default_banned_rights' => ChatBannedRights, 'participants_count' => int];
```  


Or, if you're into Lua:

```lua
channel={_='channel', creator=Bool, left=Bool, broadcast=Bool, verified=Bool, megagroup=Bool, restricted=Bool, signatures=Bool, min=Bool, scam=Bool, has_link=Bool, id=int, access_hash=long, title='string', username='string', photo=ChatPhoto, date=int, version=int, restriction_reason='string', admin_rights=ChatAdminRights, banned_rights=ChatBannedRights, default_banned_rights=ChatBannedRights, participants_count=int}

```


