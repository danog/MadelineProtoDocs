---
title: "stories.storyViews"
description: "stories.storyViews attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_storyViews.html
---
# Constructor: stories.storyViews  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|views|Array of [StoryViews](/API_docs/types/StoryViews.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [stories.StoryViews](/API_docs/types/stories.StoryViews.html)


### Example:

```
$stories_storyViews = ['_' => 'stories.storyViews', 'views' => [StoryViews, StoryViews], 'users' => [User, User]];
```  
