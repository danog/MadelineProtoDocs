---
title: "updatePinnedChannelMessages"
description: "Messages were pinned/unpinned in a channel/supergroup"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePinnedChannelMessages  
[Back to constructors index](/API_docs/constructors/index.md)



Messages were pinned/unpinned in a [channel/supergroup](https://core.telegram.org/api/channel)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pinned|[Bool](/API_docs/types/Bool.md) | Optional|Whether the messages were pinned or unpinned|
|channel\_id|[long](/API_docs/types/long.md) | Yes|
|messages|Array of [int](/API_docs/types/int.md) | Yes|Messages|
|pts|[int](/API_docs/types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updatePinnedChannelMessages = ['_' => 'updatePinnedChannelMessages', 'pinned' => Bool, 'channel_id' => long, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  
