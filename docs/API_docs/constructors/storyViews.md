---
title: "storyViews"
description: "storyViews attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyViews  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|has\_viewers|[Bool](/API_docs/types/Bool.html) | Optional|
|views\_count|[int](/API_docs/types/int.html) | Yes|
|reactions\_count|[int](/API_docs/types/int.html) | Yes|
|recent\_viewers|Array of [long](/API_docs/types/long.html) | Optional|



### Type: [StoryViews](/API_docs/types/StoryViews.html)


### Example:

```
$storyViews = ['_' => 'storyViews', 'has_viewers' => Bool, 'views_count' => int, 'reactions_count' => int, 'recent_viewers' => [long, long]];
```  
