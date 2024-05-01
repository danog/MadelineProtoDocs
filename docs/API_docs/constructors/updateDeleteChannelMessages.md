---
title: "updateDeleteChannelMessages"
description: "Some messages in a supergroup/channel were deleted"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteChannelMessages  
[Back to constructors index](/API_docs/constructors/index.html)



Some messages in a [supergroup/channel](https://core.telegram.org/api/channel) were deleted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel ID|
|messages|Array of [int](/API_docs/types/int.html) | Yes|IDs of messages that were deleted|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDeleteChannelMessages = ['_' => 'updateDeleteChannelMessages', 'channel_id' => long, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  
