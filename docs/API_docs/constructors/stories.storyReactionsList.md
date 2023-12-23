---
title: "stories.storyReactionsList"
description: "stories.storyReactionsList attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_storyReactionsList.html
---
# Constructor: stories.storyReactionsList  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|reactions|Array of [StoryReaction](/API_docs/types/StoryReaction.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|



### Type: [stories.StoryReactionsList](/API_docs/types/stories.StoryReactionsList.html)


### Example:

```
$stories_storyReactionsList = ['_' => 'stories.storyReactionsList', 'count' => int, 'reactions' => [StoryReaction, StoryReaction], 'chats' => [Chat, Chat], 'users' => [User, User], 'next_offset' => 'string'];
```  
