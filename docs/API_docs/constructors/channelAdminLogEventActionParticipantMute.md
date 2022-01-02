---
title: "channelAdminLogEventActionParticipantMute"
description: "channelAdminLogEventActionParticipantMute attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantMute  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|participant|[GroupCallParticipant](../types/GroupCallParticipant.md) | Yes|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantMute = ['_' => 'channelAdminLogEventActionParticipantMute', 'participant' => GroupCallParticipant];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionParticipantMute={_='channelAdminLogEventActionParticipantMute', participant=GroupCallParticipant}

```


