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
|democracy|[Bool](../types/Bool.md) | Optional|
|signatures|[Bool](../types/Bool.md) | Optional|Whether signatures are enabled (channels)|
|min|[Bool](../types/Bool.md) | Optional|See [min](https://core.telegram.org/api/min)|
|id|[int](../types/int.md) | Yes|ID of the channel|
|access\_hash|[long](../types/long.md) | Optional|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|username|[string](../types/string.md) | Optional|Username|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Profile photo|
|date|[int](../types/int.md) | Yes|Date when the user joined the supergroup/channel, or if the user isn't a member, its creation date|
|version|[int](../types/int.md) | Yes|Version of the channel (always `0`)|
|restriction\_reason|[string](../types/string.md) | Optional|
|admin\_rights|[ChannelAdminRights](../types/ChannelAdminRights.md) | Optional|
|banned\_rights|[ChannelBannedRights](../types/ChannelBannedRights.md) | Optional|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$channel = ['_' => 'channel', 'creator' => Bool, 'left' => Bool, 'broadcast' => Bool, 'verified' => Bool, 'megagroup' => Bool, 'restricted' => Bool, 'democracy' => Bool, 'signatures' => Bool, 'min' => Bool, 'id' => int, 'access_hash' => long, 'title' => 'string', 'username' => 'string', 'photo' => ChatPhoto, 'date' => int, 'version' => int, 'restriction_reason' => 'string', 'admin_rights' => ChannelAdminRights, 'banned_rights' => ChannelBannedRights];
```  


Or, if you're into Lua:

```lua
channel={_='channel', creator=Bool, left=Bool, broadcast=Bool, verified=Bool, megagroup=Bool, restricted=Bool, democracy=Bool, signatures=Bool, min=Bool, id=int, access_hash=long, title='string', username='string', photo=ChatPhoto, date=int, version=int, restriction_reason='string', admin_rights=ChannelAdminRights, banned_rights=ChannelBannedRights}

```


