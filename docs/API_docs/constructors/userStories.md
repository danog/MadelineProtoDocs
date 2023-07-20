---
title: "userStories"
description: "userStories attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userStories  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|max\_read\_id|[int](/API_docs/types/int.html) | Optional|
|stories|Array of [StoryItem](/API_docs/types/StoryItem.html) | Yes|



### Type: [UserStories](/API_docs/types/UserStories.html)


### Example:

```
$userStories = ['_' => 'userStories', 'user_id' => long, 'max_read_id' => int, 'stories' => [StoryItem, StoryItem]];
```  
