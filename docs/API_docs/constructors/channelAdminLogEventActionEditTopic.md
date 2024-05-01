---
title: "channelAdminLogEventActionEditTopic"
description: "A forum topic was edited"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionEditTopic  
[Back to constructors index](/API_docs/constructors/index.html)



A [forum topic](https://core.telegram.org/api/forum#forum-topics) was edited

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_topic|[ForumTopic](/API_docs/types/ForumTopic.html) | Yes|Previous topic information|
|new\_topic|[ForumTopic](/API_docs/types/ForumTopic.html) | Yes|New topic information|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionEditTopic = ['_' => 'channelAdminLogEventActionEditTopic', 'prev_topic' => ForumTopic, 'new_topic' => ForumTopic];
```  
