---
title: "updateReadChannelDiscussionInbox"
description: "Incoming comments in a discussion thread were marked as read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelDiscussionInbox  
[Back to constructors index](/API_docs/constructors/index.html)



Incoming comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|[Discussion group ID](https://core.telegram.org/api/channel)|
|top\_msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the group message that started the [thread](https://core.telegram.org/api/threads) (message in linked discussion group)|
|read\_max\_id|[int](/API_docs/types/int.html) | Yes|Message ID of latest read incoming message for this [thread](https://core.telegram.org/api/threads)|
|broadcast\_id|[long](/API_docs/types/long.html) | Optional|If set, contains the ID of the [channel](https://core.telegram.org/api/channel) that contains the post that started the [comment thread](https://core.telegram.org/api/threads) in the discussion group (`channel_id`)|
|broadcast\_post|[int](/API_docs/types/int.html) | Optional|If set, contains the ID of the channel post that started the the [comment thread](https://core.telegram.org/api/threads)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateReadChannelDiscussionInbox = ['_' => 'updateReadChannelDiscussionInbox', 'channel_id' => long, 'top_msg_id' => int, 'read_max_id' => int, 'broadcast_id' => long, 'broadcast_post' => int];
```  
