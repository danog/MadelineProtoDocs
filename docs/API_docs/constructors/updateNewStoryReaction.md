---
title: "updateNewStoryReaction"
description: "Represents a new reaction to a story."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewStoryReaction  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a new [reaction to a story](https://core.telegram.org/api/reactions#notifications-about-reactions).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|story\_id|[int](/API_docs/types/int.html) | Yes|[Story ID](https://core.telegram.org/api/stories).|
|peer|[long](/API_docs/types/long.html) | Yes|The peer where the story was posted.|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|The [reaction](https://core.telegram.org/api/reactions).|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateNewStoryReaction = ['_' => 'updateNewStoryReaction', 'story_id' => int, 'peer' => long, 'reaction' => Reaction];
```  
