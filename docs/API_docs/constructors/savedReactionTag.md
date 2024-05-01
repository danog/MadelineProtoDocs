---
title: "savedReactionTag"
description: "savedReactionTag attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: savedReactionTag  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|
|title|[string](/API_docs/types/string.html) | Optional|
|count|[int](/API_docs/types/int.html) | Yes|



### Type: [SavedReactionTag](/API_docs/types/SavedReactionTag.html)


### Example:

```
$savedReactionTag = ['_' => 'savedReactionTag', 'reaction' => Reaction, 'title' => 'string', 'count' => int];
```  
