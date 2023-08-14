---
title: "stories.allStories"
description: "stories.allStories attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_allStories.html
---
# Constructor: stories.allStories  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|has\_more|[Bool](/API_docs/types/Bool.html) | Optional|
|count|[int](/API_docs/types/int.html) | Yes|
|state|[string](/API_docs/types/string.html) | Yes|
|user\_stories|Array of [UserStories](/API_docs/types/UserStories.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|stealth\_mode|[StoriesStealthMode](/API_docs/types/StoriesStealthMode.html) | Yes|



### Type: [stories.AllStories](/API_docs/types/stories.AllStories.html)


### Example:

```
$stories_allStories = ['_' => 'stories.allStories', 'has_more' => Bool, 'count' => int, 'state' => 'string', 'user_stories' => [UserStories, UserStories], 'users' => [User, User], 'stealth_mode' => StoriesStealthMode];
```  
