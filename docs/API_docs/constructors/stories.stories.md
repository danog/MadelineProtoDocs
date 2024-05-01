---
title: "stories.stories"
description: "List of stories"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_stories.html
---
# Constructor: stories.stories  
[Back to constructors index](/API_docs/constructors/index.html)



List of [stories](https://core.telegram.org/api/stories#pinned-or-archived-stories)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of stories that can be fetched|
|stories|Array of [StoryItem](/API_docs/types/StoryItem.html) | Yes|Stories|
|pinned\_to\_top|Array of [int](/API_docs/types/int.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [stories.Stories](/API_docs/types/stories.Stories.html)


### Example:

```
$stories_stories = ['_' => 'stories.stories', 'count' => int, 'stories' => [StoryItem, StoryItem], 'pinned_to_top' => [int, int], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
