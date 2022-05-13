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
|chosen|[Bool](/API_docs/types/Bool.html) | Optional|Whether the current user sent this reaction|
|reaction|[string](/API_docs/types/string.html) | Yes|Reaction (a UTF8 emoji)|
|count|[int](/API_docs/types/int.html) | Yes|NUmber of users that reacted with this emoji|



### Type: [ReactionCount](/API_docs/types/ReactionCount.html)


### Example:

```
$reactionCount = ['_' => 'reactionCount', 'chosen' => Bool, 'reaction' => 'string', 'count' => int];
```  
