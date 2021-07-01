---
title: updateReadChannelDiscussionInbox
description: Incoming comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelDiscussionInbox  
[Back to constructors index](index.md)



Incoming comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|[Discussion group ID](https://core.telegram.org/api/channel)|
|top\_msg\_id|[int](../types/int.md) | Yes|ID of the group message that started the [thread](https://core.telegram.org/api/threads) (message in linked discussion group)|
|read\_max\_id|[int](../types/int.md) | Yes|Message ID of latest read incoming message for this [thread](https://core.telegram.org/api/threads)|
|broadcast\_id|[int](../types/int.md) | Optional|If set, contains the ID of the [channel](https://core.telegram.org/api/channel) that contains the post that started the [comment thread](https://core.telegram.org/api/threads) in the discussion group (`channel_id`)|
|broadcast\_post|[int](../types/int.md) | Optional|If set, contains the ID of the channel post that started the the [comment thread](https://core.telegram.org/api/threads)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelDiscussionInbox = ['_' => 'updateReadChannelDiscussionInbox', 'channel_id' => int, 'top_msg_id' => int, 'read_max_id' => int, 'broadcast_id' => int, 'broadcast_post' => int];
```  


Or, if you're into Lua:

```lua
updateReadChannelDiscussionInbox={_='updateReadChannelDiscussionInbox', channel_id=int, top_msg_id=int, read_max_id=int, broadcast_id=int, broadcast_post=int}

```


