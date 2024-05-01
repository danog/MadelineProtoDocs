---
title: "messageEmpty"
description: "Empty constructor, non-existent message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEmpty  
[Back to constructors index](/API_docs/constructors/index.html)



Empty constructor, non-existent message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.html) | Yes|Message identifier|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Optional|Peer ID, the chat where this message was sent|



### Type: [Message](/API_docs/types/Message.html)


### Example:

```
$messageEmpty = ['_' => 'messageEmpty', 'id' => int, 'peer_id' => Peer];
```  
