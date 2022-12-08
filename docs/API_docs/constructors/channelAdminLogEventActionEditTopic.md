---
title: "channelAdminLogEventActionEditTopic"
description: "channelAdminLogEventActionEditTopic attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionEditTopic  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|prev\_topic|[ForumTopic](/API_docs/types/ForumTopic.html) | Yes|
|new\_topic|[ForumTopic](/API_docs/types/ForumTopic.html) | Yes|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionEditTopic = ['_' => 'channelAdminLogEventActionEditTopic', 'prev_topic' => ForumTopic, 'new_topic' => ForumTopic];
```  
