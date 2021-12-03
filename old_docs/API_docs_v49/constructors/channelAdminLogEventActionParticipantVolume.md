---
title: channelAdminLogEventActionParticipantVolume
description: channelAdminLogEventActionParticipantVolume attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantVolume  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|participant|[GroupCallParticipant](../types/GroupCallParticipant.md) | Yes|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantVolume = ['_' => 'channelAdminLogEventActionParticipantVolume', 'participant' => GroupCallParticipant];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionParticipantVolume={_='channelAdminLogEventActionParticipantVolume', participant=GroupCallParticipant}

```


