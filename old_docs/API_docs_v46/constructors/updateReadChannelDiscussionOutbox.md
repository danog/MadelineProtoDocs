---
title: updateReadChannelDiscussionOutbox
description: Outgoing comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelDiscussionOutbox  
[Back to constructors index](index.md)



Outgoing comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|[Supergroup ID](https://core.telegram.org/api/channel)|
|top\_msg\_id|[int](../types/int.md) | Yes|ID of the group message that started the [thread](https://core.telegram.org/api/threads)|
|read\_max\_id|[int](../types/int.md) | Yes|Message ID of latest read outgoing message for this [thread](https://core.telegram.org/api/threads)|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelDiscussionOutbox = ['_' => 'updateReadChannelDiscussionOutbox', 'channel_id' => int, 'top_msg_id' => int, 'read_max_id' => int];
```  


Or, if you're into Lua:

```lua
updateReadChannelDiscussionOutbox={_='updateReadChannelDiscussionOutbox', channel_id=int, top_msg_id=int, read_max_id=int}

```


