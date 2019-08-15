---
title: channel
description: Channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channel  
[Back to constructors index](index.md)



Channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](../types/Bool.md) | Optional|Creator?|
|left|[Bool](../types/Bool.md) | Optional|Left?|
|broadcast|[Bool](../types/Bool.md) | Optional|Broadcast?|
|verified|[Bool](../types/Bool.md) | Optional|Verified?|
|megagroup|[Bool](../types/Bool.md) | Optional|Megagroup?|
|restricted|[Bool](../types/Bool.md) | Optional|Restricted?|
|signatures|[Bool](../types/Bool.md) | Optional|Signatures?|
|min|[Bool](../types/Bool.md) | Optional|Min?|
|scam|[Bool](../types/Bool.md) | Optional|Scam channel|
|has\_link|[Bool](../types/Bool.md) | Optional|Has linked chat?|
|has\_geo|[Bool](../types/Bool.md) | Optional||
|slowmode\_enabled|[Bool](../types/Bool.md) | Optional||
|id|[int](../types/int.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Optional|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|username|[string](../types/string.md) | Optional|Username|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Photo|
|date|[int](../types/int.md) | Yes|Date|
|version|[int](../types/int.md) | Yes|Version|
|restriction\_reason|[string](../types/string.md) | Optional|Restriction reason|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | Optional|Admin rights of current user|
|banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Optional|Banned rights of current user|
|default\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Optional|Global chat banned rights|
|participants\_count|[int](../types/int.md) | Optional|Participants count|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$channel = ['_' => 'channel', 'creator' => Bool, 'left' => Bool, 'broadcast' => Bool, 'verified' => Bool, 'megagroup' => Bool, 'restricted' => Bool, 'signatures' => Bool, 'min' => Bool, 'scam' => Bool, 'has_link' => Bool, 'has_geo' => Bool, 'slowmode_enabled' => Bool, 'id' => int, 'access_hash' => long, 'title' => 'string', 'username' => 'string', 'photo' => ChatPhoto, 'date' => int, 'version' => int, 'restriction_reason' => 'string', 'admin_rights' => ChatAdminRights, 'banned_rights' => ChatBannedRights, 'default_banned_rights' => ChatBannedRights, 'participants_count' => int];
```  


Or, if you're into Lua:

```lua
channel={_='channel', creator=Bool, left=Bool, broadcast=Bool, verified=Bool, megagroup=Bool, restricted=Bool, signatures=Bool, min=Bool, scam=Bool, has_link=Bool, has_geo=Bool, slowmode_enabled=Bool, id=int, access_hash=long, title='string', username='string', photo=ChatPhoto, date=int, version=int, restriction_reason='string', admin_rights=ChatAdminRights, banned_rights=ChatBannedRights, default_banned_rights=ChatBannedRights, participants_count=int}

```


