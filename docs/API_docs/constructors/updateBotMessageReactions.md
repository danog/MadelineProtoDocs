---
title: "updateBotMessageReactions"
description: "updateBotMessageReactions attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotMessageReactions  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[long](/API_docs/types/long.html) | Yes|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|reactions|Array of [ReactionCount](/API_docs/types/ReactionCount.html) | Yes|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotMessageReactions = ['_' => 'updateBotMessageReactions', 'peer' => long, 'msg_id' => int, 'date' => int, 'reactions' => [ReactionCount, ReactionCount], 'qts' => int];
```  
