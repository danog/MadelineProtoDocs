---
title: "stories.storyViewsList"
description: "stories.storyViewsList attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_storyViewsList.html
---
# Constructor: stories.storyViewsList  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|reactions\_count|[int](/API_docs/types/int.html) | Yes|
|views|Array of [StoryView](/API_docs/types/StoryView.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|



### Type: [stories.StoryViewsList](/API_docs/types/stories.StoryViewsList.html)


### Example:

```
$stories_storyViewsList = ['_' => 'stories.storyViewsList', 'count' => int, 'reactions_count' => int, 'views' => [StoryView, StoryView], 'users' => [User, User], 'next_offset' => 'string'];
```  
