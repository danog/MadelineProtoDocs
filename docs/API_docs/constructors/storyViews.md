---
title: "storyViews"
description: "Aggregated view and reaction information of a story."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyViews  
[Back to constructors index](/API_docs/constructors/index.html)



Aggregated view and reaction information of a [story](https://core.telegram.org/api/stories).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_viewers|[Bool](/API_docs/types/Bool.html) | Optional|If set, indicates that the viewers list is currently viewable, and was not yet deleted because the story has expired while the user didn't have a [Premium](https://core.telegram.org/api/premium) account.|
|views\_count|[int](/API_docs/types/int.html) | Yes|View counter of the story|
|forwards\_count|[int](/API_docs/types/int.html) | Optional|Forward counter of the story|
|reactions|Array of [ReactionCount](/API_docs/types/ReactionCount.html) | Optional|All reactions sent to this story|
|reactions\_count|[int](/API_docs/types/int.html) | Optional|Number of reactions added to the story|
|recent\_viewers|Array of [long](/API_docs/types/long.html) | Optional|User IDs of some recent viewers of the story|



### Type: [StoryViews](/API_docs/types/StoryViews.html)


### Example:

```
$storyViews = ['_' => 'storyViews', 'has_viewers' => Bool, 'views_count' => int, 'forwards_count' => int, 'reactions' => [ReactionCount, ReactionCount], 'reactions_count' => int, 'recent_viewers' => [long, long]];
```  
