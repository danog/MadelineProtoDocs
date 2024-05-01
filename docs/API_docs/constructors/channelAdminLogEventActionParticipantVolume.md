---
title: "channelAdminLogEventActionParticipantVolume"
description: "channelAdminLogEvent.user_id has set the volume of participant.peer to participant.volume"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantVolume  
[Back to constructors index](/API_docs/constructors/index.html)



channelAdminLogEvent.user\_id has set the volume of participant.peer to participant.volume

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[GroupCallParticipant](/API_docs/types/GroupCallParticipant.html) | Yes|The participant whose volume was changed|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantVolume = ['_' => 'channelAdminLogEventActionParticipantVolume', 'participant' => GroupCallParticipant];
```  
