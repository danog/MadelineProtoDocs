---
title: "updatePinnedChannelMessages"
description: "Messages were pinned/unpinned in a channel/supergroup"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedChannelMessages  
[Back to constructors index](/API_docs/constructors/index.html)



Messages were pinned/unpinned in a [channel/supergroup](https://core.telegram.org/api/channel)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|Whether the messages were pinned or unpinned|
|channel\_id|[long](/API_docs/types/long.html) | Yes|Channel ID|
|messages|Array of [int](/API_docs/types/int.html) | Yes|Messages|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePinnedChannelMessages = ['_' => 'updatePinnedChannelMessages', 'pinned' => Bool, 'channel_id' => long, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  
