---
title: "channelAdminLogEventActionParticipantToggleAdmin"
description: "The admin rights of a user were changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantToggleAdmin  
[Back to constructors index](/API_docs/constructors/index.html)



The admin [rights](https://core.telegram.org/api/rights) of a user were changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|Previous admin rights|
|new\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|New admin rights|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantToggleAdmin = ['_' => 'channelAdminLogEventActionParticipantToggleAdmin', 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant];
```  
