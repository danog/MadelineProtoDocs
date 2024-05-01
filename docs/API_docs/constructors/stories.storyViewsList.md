---
title: "stories.storyViewsList"
description: "Reaction and view counters for a story"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_storyViewsList.html
---
# Constructor: stories.storyViewsList  
[Back to constructors index](/API_docs/constructors/index.html)



Reaction and view counters for a [story](https://core.telegram.org/api/stories)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results that can be fetched|
|views\_count|[int](/API_docs/types/int.html) | Yes|Total number of story views|
|forwards\_count|[int](/API_docs/types/int.html) | Yes|Total number of story forwards/reposts|
|reactions\_count|[int](/API_docs/types/int.html) | Yes|Number of reactions that were added to the story|
|views|Array of [StoryView](/API_docs/types/StoryView.html) | Yes|Story view date and reaction information|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|
|next\_offset|[string](/API_docs/types/string.html) | Optional|Offset for pagination|



### Type: [stories.StoryViewsList](/API_docs/types/stories.StoryViewsList.html)


### Example:

```
$stories_storyViewsList = ['_' => 'stories.storyViewsList', 'count' => int, 'views_count' => int, 'forwards_count' => int, 'reactions_count' => int, 'views' => [StoryView, StoryView], 'chats' => [Chat, Chat], 'users' => [User, User], 'next_offset' => 'string'];
```  
