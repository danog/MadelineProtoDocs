---
title: messageReplies
description: messageReplies attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReplies  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|comments|[Bool](../types/Bool.md) | Optional|
|replies|[int](../types/int.md) | Yes|
|replies\_pts|[int](../types/int.md) | Yes|
|recent\_repliers|Array of [Peer](../types/Peer.md) | Optional|
|channel\_id|[int](../types/int.md) | Optional|
|max\_id|[int](../types/int.md) | Optional|
|read\_max\_id|[int](../types/int.md) | Optional|



### Type: [MessageReplies](../types/MessageReplies.md)


### Example:

```php
$messageReplies = ['_' => 'messageReplies', 'comments' => Bool, 'replies' => int, 'replies_pts' => int, 'recent_repliers' => [Peer, Peer], 'channel_id' => int, 'max_id' => int, 'read_max_id' => int];
```  


Or, if you're into Lua:

```lua
messageReplies={_='messageReplies', comments=Bool, replies=int, replies_pts=int, recent_repliers={Peer}, channel_id=int, max_id=int, read_max_id=int}

```


