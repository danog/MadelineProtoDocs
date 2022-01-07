---
title: "updateReadChannelDiscussionOutbox"
description: "Outgoing comments in a discussion thread were marked as read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelDiscussionOutbox  
[Back to constructors index](index.md)



Outgoing comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](../types/long.md) | Yes|
|top\_msg\_id|[int](../types/int.md) | Yes|ID of the group message that started the [thread](https://core.telegram.org/api/threads)|
|read\_max\_id|[int](../types/int.md) | Yes|Message ID of latest read outgoing message for this [thread](https://core.telegram.org/api/threads)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelDiscussionOutbox = ['_' => 'updateReadChannelDiscussionOutbox', 'channel_id' => long, 'top_msg_id' => int, 'read_max_id' => int];
```  
