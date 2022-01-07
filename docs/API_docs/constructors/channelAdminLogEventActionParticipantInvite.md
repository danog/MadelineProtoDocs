---
title: "channelAdminLogEventActionParticipantInvite"
description: "A user was invited to the group"
nav_exclude: true
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
