---
title: "updateChannelPinnedTopics"
description: "The pinned topics of a forum have changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelPinnedTopics  
[Back to constructors index](/API_docs/constructors/index.html)



The [pinned topics](https://core.telegram.org/api/forum#forum-topics) of a forum have changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Forum ID.|
|order|Array of [int](/API_docs/types/int.html) | Optional|Ordered list containing the IDs of all pinned topics.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelPinnedTopics = ['_' => 'updateChannelPinnedTopics', 'channel_id' => long, 'order' => [int, int]];
```  
