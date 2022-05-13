---
title: "channelAdminLogEvent"
description: "Admin log event"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEvent  
[Back to constructors index](/API_docs/constructors/index.html)



Admin log event

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Event ID|
|date|[int](/API_docs/types/int.html) | Yes|Date|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|action|[ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html) | Yes|Action|



### Type: [ChannelAdminLogEvent](/API_docs/types/ChannelAdminLogEvent.html)


### Example:

```
$channelAdminLogEvent = ['_' => 'channelAdminLogEvent', 'id' => long, 'date' => int, 'user_id' => long, 'action' => ChannelAdminLogEventAction];
```  
