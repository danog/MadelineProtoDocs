---
title: updateDeleteChannelMessages
description: Some messages in a [supergroup/channel](https://core.telegram.org/api/channel) were deleted
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateDeleteChannelMessages  
[Back to constructors index](index.md)



Some messages in a [supergroup/channel](https://core.telegram.org/api/channel) were deleted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|messages|Array of [int](../types/int.md) | Yes|IDs of messages that were deleted|
|channel\_pts|[int](../types/int.md) | Yes|
|channel\_pts\_count|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateDeleteChannelMessages = ['_' => 'updateDeleteChannelMessages', 'channel_id' => int, 'messages' => [int, int], 'channel_pts' => int, 'channel_pts_count' => int];
```  


Or, if you're into Lua:

```lua
updateDeleteChannelMessages={_='updateDeleteChannelMessages', channel_id=int, messages={int}, channel_pts=int, channel_pts_count=int}

```


