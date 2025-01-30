---
title: "channelAdminLogEventActionParticipantSubExtend"
description: "A paid subscriber has extended their Telegram Star subscription »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantSubExtend  
[Back to constructors index](/API_docs/constructors/index.html)



A paid subscriber has extended their [Telegram Star subscription »](https://core.telegram.org/api/stars#star-subscriptions).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|Same as `new_participant`.|
|new\_participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|The subscriber that extended the subscription.|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantSubExtend = ['_' => 'channelAdminLogEventActionParticipantSubExtend', 'prev_participant' => ChannelParticipant, 'new_participant' => ChannelParticipant];
```  
