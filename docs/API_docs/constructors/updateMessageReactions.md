---
title: "updateMessageReactions"
description: "New message reactions » are available"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageReactions  
[Back to constructors index](/API_docs/constructors/index.html)



New [message reactions »](https://core.telegram.org/api/reactions) are available

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Peer|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID|
|top\_msg\_id|[int](/API_docs/types/int.html) | Optional|[Forum topic ID](https://core.telegram.org/api/forum#forum-topics)|
|saved\_peer\_id|[Peer](/API_docs/types/Peer.html) | Optional|If set, the reactions are in the specified [monoforum topic »](https://core.telegram.org/api/monoforum).|
|reactions|[MessageReactions](/API_docs/types/MessageReactions.html) | Yes|Reactions|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessageReactions = ['_' => 'updateMessageReactions', 'peer' => long, 'msg_id' => int, 'top_msg_id' => int, 'saved_peer_id' => Peer, 'reactions' => MessageReactions];
```  
