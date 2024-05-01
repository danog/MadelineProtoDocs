---
title: "updateNewStoryReaction"
description: "updateNewStoryReaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewStoryReaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|story\_id|[int](/API_docs/types/int.html) | Yes|
|peer|[long](/API_docs/types/long.html) | Yes|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNewStoryReaction = ['_' => 'updateNewStoryReaction', 'story_id' => int, 'peer' => long, 'reaction' => Reaction];
```  
