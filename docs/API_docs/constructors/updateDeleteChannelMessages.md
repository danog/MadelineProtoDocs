---
title: "updateDeleteChannelMessages"
description: "Some messages in a supergroup/channel were deleted"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteChannelMessages  
[Back to constructors index](index.md)



Some messages in a [supergroup/channel](https://core.telegram.org/api/channel) were deleted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](../types/long.md) | Yes|
|messages|Array of [int](../types/int.md) | Yes|IDs of messages that were deleted|
|pts|[int](../types/int.md) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](../types/int.md) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDeleteChannelMessages = ['_' => 'updateDeleteChannelMessages', 'channel_id' => long, 'messages' => [int, int], 'pts' => int, 'pts_count' => int];
```  
