---
title: messageReplies
description: Info about [the comment section of a channel post, or a simple message thread](https://core.telegram.org/api/threads)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReplies  
[Back to constructors index](index.md)



Info about [the comment section of a channel post, or a simple message thread](https://core.telegram.org/api/threads)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|comments|[Bool](../types/Bool.md) | Optional|Whether this constructor contains information about the [comment section of a channel post, or a simple message thread](https://core.telegram.org/api/threads)|
|replies|[int](../types/int.md) | Yes|Contains the total number of replies in this thread or comment section.|
|replies\_pts|[int](../types/int.md) | Yes|[PTS](https://core.telegram.org/api/updates) of the message that started this thread.|
|recent\_repliers|Array of [Peer](../types/Peer.md) | Optional|For channel post comments, contains information about the last few comment posters for a specific thread, to show a small list of commenter profile pictures in client previews.|
|channel\_id|[long](../types/long.md) | Optional|
|max\_id|[int](../types/int.md) | Optional|ID of the latest message in this thread or comment section.|
|read\_max\_id|[int](../types/int.md) | Optional|Contains the ID of the latest read message in this thread or comment section.|



### Type: [MessageReplies](../types/MessageReplies.md)


### Example:

```php
$messageReplies = ['_' => 'messageReplies', 'comments' => Bool, 'replies' => int, 'replies_pts' => int, 'recent_repliers' => [Peer, Peer], 'channel_id' => long, 'max_id' => int, 'read_max_id' => int];
```  


Or, if you're into Lua:

```lua
messageReplies={_='messageReplies', comments=Bool, replies=int, replies_pts=int, recent_repliers={Peer}, channel_id=long, max_id=int, read_max_id=int}

```


