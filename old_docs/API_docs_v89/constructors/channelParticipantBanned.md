---
title: channelParticipantBanned
description: Channel participant banned
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantBanned  
[Back to constructors index](index.md)



Channel participant banned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|left|[Bool](../types/Bool.md) | Optional|Left?|
|user\_id|[int](../types/int.md) | Yes|User ID|
|kicked\_by|[int](../types/int.md) | Yes|Kicked by|
|date|[int](../types/int.md) | Yes|Date|
|banned\_rights|[ChannelBannedRights](../types/ChannelBannedRights.md) | Yes|Banned rights|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantBanned = ['_' => 'channelParticipantBanned', 'left' => Bool, 'user_id' => int, 'kicked_by' => int, 'date' => int, 'banned_rights' => ChannelBannedRights];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelParticipantBanned", "left": Bool, "user_id": int, "kicked_by": int, "date": int, "banned_rights": ChannelBannedRights}
```


Or, if you're into Lua:

```lua
channelParticipantBanned={_='channelParticipantBanned', left=Bool, user_id=int, kicked_by=int, date=int, banned_rights=ChannelBannedRights}

```


