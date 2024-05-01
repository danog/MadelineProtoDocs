---
title: "channelAdminLogEventActionParticipantUnmute"
description: "A group call participant was unmuted"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantUnmute  
[Back to constructors index](/API_docs/constructors/index.html)



A group call participant was unmuted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|The participant that was unmuted|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantUnmute = ['_' => 'channelAdminLogEventActionParticipantUnmute', 'participant' => GroupCallParticipant];
```  
