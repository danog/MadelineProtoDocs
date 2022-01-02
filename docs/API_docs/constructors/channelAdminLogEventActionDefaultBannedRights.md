---
title: "channelAdminLogEventActionDefaultBannedRights"
description: "The default banned rights were modified"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionDefaultBannedRights  
[Back to constructors index](index.md)



The default banned rights were modified

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Yes|Previous global [banned rights](https://core.telegram.org/api/rights)|
|new\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Yes|New glboal [banned rights](https://core.telegram.org/api/rights).|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionDefaultBannedRights = ['_' => 'channelAdminLogEventActionDefaultBannedRights', 'prev_banned_rights' => ChatBannedRights, 'new_banned_rights' => ChatBannedRights];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionDefaultBannedRights={_='channelAdminLogEventActionDefaultBannedRights', prev_banned_rights=ChatBannedRights, new_banned_rights=ChatBannedRights}

```


