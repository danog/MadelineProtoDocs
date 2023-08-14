---
title: "updateSentStoryReaction"
description: "updateSentStoryReaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateSentStoryReaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|story\_id|[int](/API_docs/types/int.html) | Yes|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateSentStoryReaction = ['_' => 'updateSentStoryReaction', 'user_id' => long, 'story_id' => int, 'reaction' => Reaction];
```  
