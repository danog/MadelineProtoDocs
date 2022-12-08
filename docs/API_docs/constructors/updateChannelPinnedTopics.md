---
title: "updateChannelPinnedTopics"
description: "updateChannelPinnedTopics attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateChannelPinnedTopics  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|
|order|Array of [int](/API_docs/types/int.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateChannelPinnedTopics = ['_' => 'updateChannelPinnedTopics', 'channel_id' => long, 'order' => [int, int]];
```  
