---
title: "updateBotMessageReactions"
description: "Bots only: the number of reactions on a message with anonymous reactions has changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotMessageReactions  
[Back to constructors index](/API_docs/constructors/index.html)



Bots only: the number of reactions on a message with anonymous reactions has changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Peer of the reacted-to message.|
|msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the reacted-to message.|
|date|[int](/API_docs/types/int.html) | Yes|Date of the change.|
|reactions|Array of [ReactionCount](/API_docs/types/ReactionCount.html) | Yes|New reaction counters.|
|qts|[int](/API_docs/types/int.html) | Yes|[QTS](https://core.telegram.org/api/updates) event sequence identifier|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotMessageReactions = ['_' => 'updateBotMessageReactions', 'peer' => long, 'msg_id' => int, 'date' => int, 'reactions' => [ReactionCount, ReactionCount], 'qts' => int];
```  
