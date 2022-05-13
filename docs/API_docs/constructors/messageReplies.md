---
title: "messageReplies"
description: "Info about the comment section of a channel post, or a simple message thread"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReplies  
[Back to constructors index](/API_docs/constructors/index.html)



Info about [the comment section of a channel post, or a simple message thread](https://core.telegram.org/api/threads)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|comments|[Bool](/API_docs/types/Bool.html) | Optional|Whether this constructor contains information about the [comment section of a channel post, or a simple message thread](https://core.telegram.org/api/threads)|
|replies|[int](/API_docs/types/int.html) | Yes|Contains the total number of replies in this thread or comment section.|
|replies\_pts|[int](/API_docs/types/int.html) | Yes|[PTS](https://core.telegram.org/api/updates) of the message that started this thread.|
|recent\_repliers|Array of [Peer](/API_docs/types/Peer.html) | Optional|For channel post comments, contains information about the last few comment posters for a specific thread, to show a small list of commenter profile pictures in client previews.|
|channel\_id|[long](/API_docs/types/long.html) | Optional|For channel post comments, contains the ID of the associated [discussion supergroup](https://core.telegram.org/api/discussion)|
|max\_id|[int](/API_docs/types/int.html) | Optional|ID of the latest message in this thread or comment section.|
|read\_max\_id|[int](/API_docs/types/int.html) | Optional|Contains the ID of the latest read message in this thread or comment section.|



### Type: [MessageReplies](/API_docs/types/MessageReplies.html)


### Example:

```
$messageReplies = ['_' => 'messageReplies', 'comments' => Bool, 'replies' => int, 'replies_pts' => int, 'recent_repliers' => [Peer, Peer], 'channel_id' => long, 'max_id' => int, 'read_max_id' => int];
```  
