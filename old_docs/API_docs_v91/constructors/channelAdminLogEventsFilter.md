---
title: channelAdminLogEventsFilter
description: Event filter
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventsFilter  
[Back to constructors index](index.md)



Event filter

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|join|[Bool](../types/Bool.md) | Optional|Join users events|
|leave|[Bool](../types/Bool.md) | Optional|Left users events|
|invite|[Bool](../types/Bool.md) | Optional|Invite users events|
|ban|[Bool](../types/Bool.md) | Optional|Ban events|
|unban|[Bool](../types/Bool.md) | Optional|Unban events|
|kick|[Bool](../types/Bool.md) | Optional|Kicked users events|
|unkick|[Bool](../types/Bool.md) | Optional|Unkick events|
|promote|[Bool](../types/Bool.md) | Optional|Admin promotion events|
|demote|[Bool](../types/Bool.md) | Optional|Demote admin events|
|info|[Bool](../types/Bool.md) | Optional|Change info events|
|settings|[Bool](../types/Bool.md) | Optional|Setting changes|
|pinned|[Bool](../types/Bool.md) | Optional|Pinned message events|
|edit|[Bool](../types/Bool.md) | Optional|Edit message events|
|delete|[Bool](../types/Bool.md) | Optional|Delete message events|



### Type: [ChannelAdminLogEventsFilter](../types/ChannelAdminLogEventsFilter.md)


### Example:

```php
$channelAdminLogEventsFilter = ['_' => 'channelAdminLogEventsFilter', 'join' => Bool, 'leave' => Bool, 'invite' => Bool, 'ban' => Bool, 'unban' => Bool, 'kick' => Bool, 'unkick' => Bool, 'promote' => Bool, 'demote' => Bool, 'info' => Bool, 'settings' => Bool, 'pinned' => Bool, 'edit' => Bool, 'delete' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelAdminLogEventsFilter", "join": Bool, "leave": Bool, "invite": Bool, "ban": Bool, "unban": Bool, "kick": Bool, "unkick": Bool, "promote": Bool, "demote": Bool, "info": Bool, "settings": Bool, "pinned": Bool, "edit": Bool, "delete": Bool}
```


Or, if you're into Lua:

```lua
channelAdminLogEventsFilter={_='channelAdminLogEventsFilter', join=Bool, leave=Bool, invite=Bool, ban=Bool, unban=Bool, kick=Bool, unkick=Bool, promote=Bool, demote=Bool, info=Bool, settings=Bool, pinned=Bool, edit=Bool, delete=Bool}

```


