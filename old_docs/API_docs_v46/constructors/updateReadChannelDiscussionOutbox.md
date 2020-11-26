---
title: updateReadChannelDiscussionOutbox
description: updateReadChannelDiscussionOutbox attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelDiscussionOutbox  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[int](../types/int.md) | Yes|
|top\_msg\_id|[int](../types/int.md) | Yes|
|read\_max\_id|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelDiscussionOutbox = ['_' => 'updateReadChannelDiscussionOutbox', 'channel_id' => int, 'top_msg_id' => int, 'read_max_id' => int];
```  


Or, if you're into Lua:

```lua
updateReadChannelDiscussionOutbox={_='updateReadChannelDiscussionOutbox', channel_id=int, top_msg_id=int, read_max_id=int}

```


