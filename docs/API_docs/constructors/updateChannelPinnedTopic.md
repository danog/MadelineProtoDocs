---
title: "updateChannelPinnedTopic"
description: "A forum topic » was pinned or unpinned."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelPinnedTopic  
[Back to constructors index](/API_docs/constructors/index.html)



A [forum topic »](https://core.telegram.org/api/forum#forum-topics) was pinned or unpinned.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|Whether the topic was pinned or unpinned|
|channel\_id|[long](/API_docs/types/long.html) | Yes|The forum ID|
|topic\_id|[int](/API_docs/types/int.html) | Yes|The topic ID|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelPinnedTopic = ['_' => 'updateChannelPinnedTopic', 'pinned' => Bool, 'channel_id' => long, 'topic_id' => int];
```  
