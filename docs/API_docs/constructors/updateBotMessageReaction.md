---
title: "updateBotMessageReaction"
description: "Bots only: a user has changed their reactions on a message with public reactions."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotMessageReaction  
[Back to constructors index](/API_docs/constructors/index.html)



Bots only: a user has changed their reactions on a message with public reactions.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Peer of the reacted-to message.|
|msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the reacted-to message.|
|date|[int](/API_docs/types/int.html) | Yes|Date of the change.|
|actor|[Peer](/API_docs/types/Peer.html) | Yes|The user that (un)reacted to the message.|
|old\_reactions|Array of [Reaction](/API_docs/types/Reaction.html) | Yes|Old reactions|
|new\_reactions|Array of [Reaction](/API_docs/types/Reaction.html) | Yes|New reactions|
|qts|[int](/API_docs/types/int.html) | Yes|[QTS](https://core.telegram.org/api/updates) event sequence identifier|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotMessageReaction = ['_' => 'updateBotMessageReaction', 'peer' => long, 'msg_id' => int, 'date' => int, 'actor' => Peer, 'old_reactions' => [Reaction, Reaction], 'new_reactions' => [Reaction, Reaction], 'qts' => int];
```  
