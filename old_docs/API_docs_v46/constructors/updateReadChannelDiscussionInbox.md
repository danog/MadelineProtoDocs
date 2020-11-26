---
title: updateReadChannelDiscussionInbox
description: updateReadChannelDiscussionInbox attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelDiscussionInbox  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[int](../types/int.md) | Yes|
|top\_msg\_id|[int](../types/int.md) | Yes|
|read\_max\_id|[int](../types/int.md) | Yes|
|broadcast\_id|[int](../types/int.md) | Optional|
|broadcast\_post|[int](../types/int.md) | Optional|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelDiscussionInbox = ['_' => 'updateReadChannelDiscussionInbox', 'channel_id' => int, 'top_msg_id' => int, 'read_max_id' => int, 'broadcast_id' => int, 'broadcast_post' => int];
```  


Or, if you're into Lua:

```lua
updateReadChannelDiscussionInbox={_='updateReadChannelDiscussionInbox', channel_id=int, top_msg_id=int, read_max_id=int, broadcast_id=int, broadcast_post=int}

```


