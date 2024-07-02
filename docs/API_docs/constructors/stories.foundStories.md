---
title: "stories.foundStories"
description: "stories.foundStories attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_foundStories.html
---
# Constructor: stories.foundStories  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|stories|Array of [FoundStory](/API_docs/types/FoundStory.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [stories.FoundStories](/API_docs/types/stories.FoundStories.html)


### Example:

```
$stories_foundStories = ['_' => 'stories.foundStories', 'count' => int, 'stories' => [FoundStory, FoundStory], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
