---
title: "stories.storyViews"
description: "Reaction and view counters for a list of stories"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_storyViews.html
---
# Constructor: stories.storyViews  
[Back to constructors index](/API_docs/constructors/index.html)



Reaction and view counters for a list of [stories](https://core.telegram.org/api/stories)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|views|Array of [StoryViews](/API_docs/types/StoryViews.html) | Yes|View date and reaction information of multiple stories|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [stories.StoryViews](/API_docs/types/stories.StoryViews.html)


### Example:

```
$stories_storyViews = ['_' => 'stories.storyViews', 'views' => [StoryViews, StoryViews], 'users' => [User, User]];
```  
