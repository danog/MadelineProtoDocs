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
|chosen\_order|[int](/API_docs/types/int.html) | Optional|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|
|count|[int](/API_docs/types/int.html) | Yes|NUmber of users that reacted with this emoji|



### Type: [ReactionCount](/API_docs/types/ReactionCount.html)


### Example:

```
$reactionCount = ['_' => 'reactionCount', 'chosen_order' => int, 'reaction' => Reaction, 'count' => int];
```  
