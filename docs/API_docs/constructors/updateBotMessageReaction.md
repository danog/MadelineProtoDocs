---
title: "updateBotMessageReaction"
description: "updateBotMessageReaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotMessageReaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[long](/API_docs/types/long.html) | Yes|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|actor|[Peer](/API_docs/types/Peer.html) | Yes|
|old\_reactions|Array of [Reaction](/API_docs/types/Reaction.html) | Yes|
|new\_reactions|Array of [Reaction](/API_docs/types/Reaction.html) | Yes|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotMessageReaction = ['_' => 'updateBotMessageReaction', 'peer' => long, 'msg_id' => int, 'date' => int, 'actor' => Peer, 'old_reactions' => [Reaction, Reaction], 'new_reactions' => [Reaction, Reaction], 'qts' => int];
```  
