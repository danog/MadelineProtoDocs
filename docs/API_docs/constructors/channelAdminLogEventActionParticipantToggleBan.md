---
title: "channelAdminLogEventActionParticipantToggleBan"
description: "The banned rights of a user were changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantToggleBan  
[Back to constructors index](/API_docs/constructors/index.html)



The banned [rights](https://core.telegram.org/api/rights) of a user were changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|Old banned rights of user|
|new\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|New banned rights of user|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantToggleBan = ['_' => 'channelAdminLogEventActionParticipantToggleBan', 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant];
```  
