---
title: "channelAdminLogEventActionParticipantSubExtend"
description: "channelAdminLogEventActionParticipantSubExtend attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantSubExtend  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|prev\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|
|new\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantSubExtend = ['_' => 'channelAdminLogEventActionParticipantSubExtend', 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant];
```  
