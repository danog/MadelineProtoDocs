---
title: "channelAdminLogEventActionParticipantInvite"
description: "A user was invited to the group"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantInvite  
[Back to constructors index](/API_docs/constructors/index.html)



A user was invited to the group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|The user that was invited|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantInvite = ['_' => 'channelAdminLogEventActionParticipantInvite', 'participant' => ChannelParticipant];
```  
