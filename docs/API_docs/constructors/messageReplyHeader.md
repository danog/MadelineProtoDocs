---
title: "messageReplyHeader"
description: "Message replies and thread information"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReplyHeader  
[Back to constructors index](/API_docs/constructors/index.html)



Message replies and [thread](https://core.telegram.org/api/threads) information

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|reply\_to\_scheduled|[Bool](/API_docs/types/Bool.html) | Optional|
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | Yes|ID of message to which this message is replying|
|reply\_to\_peer\_id|[Peer](/API_docs/types/Peer.html) | Optional|For replies sent in [channel discussion threads](https://core.telegram.org/api/threads) of which the current user is not a member, the discussion group ID|
|reply\_to\_top\_id|[int](/API_docs/types/int.html) | Optional|ID of the message that started this [message thread](https://core.telegram.org/api/threads)|



### Type: [MessageReplyHeader](/API_docs/types/MessageReplyHeader.html)


### Example:

```
$messageReplyHeader = ['_' => 'messageReplyHeader', 'reply_to_scheduled' => Bool, 'reply_to_msg_id' => int, 'reply_to_peer_id' => Peer, 'reply_to_top_id' => int];
```  
