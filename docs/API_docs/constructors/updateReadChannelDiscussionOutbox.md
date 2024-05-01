---
title: "updateReadChannelDiscussionOutbox"
description: "Outgoing comments in a discussion thread were marked as read"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelDiscussionOutbox  
[Back to constructors index](/API_docs/constructors/index.html)



Outgoing comments in a [discussion thread](https://core.telegram.org/api/threads) were marked as read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|[Supergroup ID](https://core.telegram.org/api/channel)|
|top\_msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the group message that started the [thread](https://core.telegram.org/api/threads)|
|read\_max\_id|[int](/API_docs/types/int.html) | Yes|Message ID of latest read outgoing message for this [thread](https://core.telegram.org/api/threads)|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateReadChannelDiscussionOutbox = ['_' => 'updateReadChannelDiscussionOutbox', 'channel_id' => long, 'top_msg_id' => int, 'read_max_id' => int];
```  
