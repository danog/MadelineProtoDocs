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
|peer|[Peer](/API_docs/types/Peer.html) | Yes|Peer|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID|
|reactions|[MessageReactions](/API_docs/types/MessageReactions.html) | Yes|Reactions|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessageReactions = ['_' => 'updateMessageReactions', 'peer' => Peer, 'msg_id' => int, 'reactions' => MessageReactions];
```  
