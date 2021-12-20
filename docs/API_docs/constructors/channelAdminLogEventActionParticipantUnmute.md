---
title: "channelAdminLogEventActionParticipantUnmute"
description: "channelAdminLogEventActionParticipantUnmute attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantUnmute  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|participant|[GroupCallParticipant](../types/GroupCallParticipant.md) | Yes|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantUnmute = ['_' => 'channelAdminLogEventActionParticipantUnmute', 'participant' => GroupCallParticipant];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionParticipantUnmute={_='channelAdminLogEventActionParticipantUnmute', participant=GroupCallParticipant}

```


