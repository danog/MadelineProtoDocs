---
title: channelAdminLogEventActionParticipantToggleBan
description: User banned
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantToggleBan  
[Back to constructors index](index.md)



User banned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|Prev participant|
|new\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|New participant|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantToggleBan = ['_' => 'channelAdminLogEventActionParticipantToggleBan', 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelAdminLogEventActionParticipantToggleBan", "prev_participant": ChannelParticipant, "new_participant": ChannelParticipant}
```


Or, if you're into Lua:

```lua
channelAdminLogEventActionParticipantToggleBan={_='channelAdminLogEventActionParticipantToggleBan', prev_participant=ChannelParticipant, new_participant=ChannelParticipant}

```


