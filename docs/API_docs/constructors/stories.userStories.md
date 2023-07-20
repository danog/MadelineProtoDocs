---
title: "stories.userStories"
description: "stories.userStories attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_userStories.html
---
# Constructor: stories.userStories  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stories|[UserStories](/API_docs/types/UserStories.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [stories.UserStories](/API_docs/types/stories.UserStories.html)


### Example:

```
$stories_userStories = ['_' => 'stories.userStories', 'stories' => UserStories, 'users' => [User, User]];
```  
