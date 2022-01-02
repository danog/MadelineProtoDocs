---
title: "channelAdminLogEventActionParticipantToggleBan"
description: "The banned rights of a user were changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantToggleBan  
[Back to constructors index](index.md)



The banned [rights](https://core.telegram.org/api/rights) of a user were changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|Old banned rights of user|
|new\_participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|New banned rights of user|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantToggleBan = ['_' => 'channelAdminLogEventActionParticipantToggleBan', 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionParticipantToggleBan={_='channelAdminLogEventActionParticipantToggleBan', prev_participant=ChannelParticipant, new_participant=ChannelParticipant}

```


