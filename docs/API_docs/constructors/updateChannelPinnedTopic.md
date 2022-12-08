---
title: "updateChannelPinnedTopic"
description: "updateChannelPinnedTopic attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelPinnedTopic  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|
|channel\_id|[long](/API_docs/types/long.html) | Yes|
|topic\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelPinnedTopic = ['_' => 'updateChannelPinnedTopic', 'pinned' => Bool, 'channel_id' => long, 'topic_id' => int];
```  
