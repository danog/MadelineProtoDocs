---
title: "postInteractionCountersStory"
description: "Interaction counters for a story."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: postInteractionCountersStory  
[Back to constructors index](/API_docs/constructors/index.html)



Interaction counters for a story.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|story\_id|[int](/API_docs/types/int.html) | Yes|Story ID|
|views|[int](/API_docs/types/int.html) | Yes|Number of views|
|forwards|[int](/API_docs/types/int.html) | Yes|Number of forwards and reposts to public chats and channels|
|reactions|[int](/API_docs/types/int.html) | Yes|Number of reactions|



### Type: [PostInteractionCounters](/API_docs/types/PostInteractionCounters.html)


### Example:

```
$postInteractionCountersStory = ['_' => 'postInteractionCountersStory', 'story_id' => int, 'views' => int, 'forwards' => int, 'reactions' => int];
```  
