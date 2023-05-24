---
title: "channelAdminLogEventActionPinTopic"
description: "A forum topic was pinned or unpinned"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionPinTopic  
[Back to constructors index](/API_docs/constructors/index.html)



A [forum topic](https://core.telegram.org/api/forum#forum-topics) was pinned or unpinned

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_topic|[ForumTopic](/API_docs/types/ForumTopic.html) | Optional|Previous topic information|
|new\_topic|[ForumTopic](/API_docs/types/ForumTopic.html) | Optional|New topic information|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionPinTopic = ['_' => 'channelAdminLogEventActionPinTopic', 'prev_topic' => ForumTopic, 'new_topic' => ForumTopic];
```  
