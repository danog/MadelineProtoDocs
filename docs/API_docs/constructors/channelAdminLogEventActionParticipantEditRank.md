---
title: "channelAdminLogEventActionParticipantEditRank"
description: "channelAdminLogEventActionParticipantEditRank attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionParticipantEditRank  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|prev\_rank|[string](/API_docs/types/string.html) | Yes|
|new\_rank|[string](/API_docs/types/string.html) | Yes|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionParticipantEditRank = ['_' => 'channelAdminLogEventActionParticipantEditRank', 'user_id' => long, 'prev_rank' => 'string', 'new_rank' => 'string'];
```  
