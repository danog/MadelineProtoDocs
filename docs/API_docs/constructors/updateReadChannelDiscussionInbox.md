---
title: "updateReadChannelDiscussionInbox"
description: "Incoming comments in a discussion thread were marked as read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelDiscussionInbox  
[Back to constructors index](index.md)



Incoming comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](../types/long.md) | Yes|
|top\_msg\_id|[int](../types/int.md) | Yes|ID of the group message that started the [thread](https://core.telegram.org/api/threads) (message in linked discussion group)|
|read\_max\_id|[int](../types/int.md) | Yes|Message ID of latest read incoming message for this [thread](https://core.telegram.org/api/threads)|
|broadcast\_id|[long](../types/long.md) | Optional|
|broadcast\_post|[int](../types/int.md) | Optional|If set, contains the ID of the channel post that started the the [comment thread](https://core.telegram.org/api/threads)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelDiscussionInbox = ['_' => 'updateReadChannelDiscussionInbox', 'channel_id' => long, 'top_msg_id' => int, 'read_max_id' => int, 'broadcast_id' => long, 'broadcast_post' => int];
```  
