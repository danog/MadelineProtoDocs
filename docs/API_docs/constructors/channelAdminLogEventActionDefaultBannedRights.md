---
title: channelAdminLogEventActionDefaultBannedRights
description: Changed global chat rights
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionDefaultBannedRights  
[Back to constructors index](index.md)



Changed global chat rights

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Yes|Previous Banned rights of current user|
|new\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Yes|New Banned rights of current user|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionDefaultBannedRights = ['_' => 'channelAdminLogEventActionDefaultBannedRights', 'prev_banned_rights' => ChatBannedRights, 'new_banned_rights' => ChatBannedRights];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelAdminLogEventActionDefaultBannedRights", "prev_banned_rights": ChatBannedRights, "new_banned_rights": ChatBannedRights}
```


Or, if you're into Lua:

```lua
channelAdminLogEventActionDefaultBannedRights={_='channelAdminLogEventActionDefaultBannedRights', prev_banned_rights=ChatBannedRights, new_banned_rights=ChatBannedRights}

```


