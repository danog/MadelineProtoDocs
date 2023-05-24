---
title: "reactionCount"
description: "Reactions"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: reactionCount  
[Back to constructors index](/API_docs/constructors/index.html)



Reactions

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chosen\_order|[int](/API_docs/types/int.html) | Optional|If set, indicates that the current user also sent this reaction. <br>The integer value indicates when was the reaction added: the bigger the value, the newer the reaction.|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|Reaction (a UTF8 emoji)|
|count|[int](/API_docs/types/int.html) | Yes|NUmber of users that reacted with this emoji|



### Type: [ReactionCount](/API_docs/types/ReactionCount.html)


### Example:

```
$reactionCount = ['_' => 'reactionCount', 'chosen_order' => int, 'reaction' => Reaction, 'count' => int];
```  
