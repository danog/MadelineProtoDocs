---
title: "stories.stories"
description: "stories.stories attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_stories.html
---
# Constructor: stories.stories  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|stories|Array of [StoryItem](/API_docs/types/StoryItem.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [stories.Stories](/API_docs/types/stories.Stories.html)


### Example:

```
$stories_stories = ['_' => 'stories.stories', 'count' => int, 'stories' => [StoryItem, StoryItem], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
