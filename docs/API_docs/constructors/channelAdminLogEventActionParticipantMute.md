---
title: "channelAdminLogEventActionParticipantMute"
description: "A group call participant was muted"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantMute  
[Back to constructors index](/API_docs/constructors/index.html)



A group call participant was muted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|The participant that was muted|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantMute = ['_' => 'channelAdminLogEventActionParticipantMute', 'participant' => GroupCallParticipant];
```  
