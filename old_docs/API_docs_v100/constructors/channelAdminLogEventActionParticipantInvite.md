---
title: channelAdminLogEventActionParticipantInvite
description: A user was invited to the group
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantInvite  
[Back to constructors index](index.md)



A user was invited to the group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|The user that was invited|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionParticipantInvite = ['_' => 'channelAdminLogEventActionParticipantInvite', 'participant' => ChannelParticipant];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionParticipantInvite={_='channelAdminLogEventActionParticipantInvite', participant=ChannelParticipant}

```


