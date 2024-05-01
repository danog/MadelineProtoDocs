---
title: "updateSentStoryReaction"
description: "Indicates we reacted to a story »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateSentStoryReaction  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates we [reacted to a story »](https://core.telegram.org/api/stories#reactions).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The peer that sent the story|
|story\_id|[int](/API_docs/types/int.html) | Yes|ID of the story we reacted to|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|The reaction that was sent|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateSentStoryReaction = ['_' => 'updateSentStoryReaction', 'peer' => long, 'story_id' => int, 'reaction' => Reaction];
```  
