---
title: "storyView"
description: "Story view date and reaction information"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyView  
[Back to constructors index](/API_docs/constructors/index.html)



[Story](https://core.telegram.org/api/stories) view date and reaction information

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|[Bool](/API_docs/types/Bool.html) | Optional|Whether we have [completely blocked](https://core.telegram.org/api/block) this user, including from viewing more of our stories.|
|blocked\_my\_stories\_from|[Bool](/API_docs/types/Bool.html) | Optional|Whether we have [blocked](https://core.telegram.org/api/block) this user from viewing more of our stories.|
|user\_id|[long](/API_docs/types/long.html) | Yes|The user that viewed the story|
|date|[int](/API_docs/types/int.html) | Yes|When did the user view the story|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|If present, contains the reaction that the user left on the story|



### Type: [StoryView](/API_docs/types/StoryView.html)


### Example:

```
$storyView = ['_' => 'storyView', 'blocked' => Bool, 'blocked_my_stories_from' => Bool, 'user_id' => long, 'date' => int, 'reaction' => Reaction];
```  
