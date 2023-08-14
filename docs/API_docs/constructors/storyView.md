---
title: "storyView"
description: "storyView attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyView  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|blocked|[Bool](/API_docs/types/Bool.html) | Optional|
|blocked\_my\_stories\_from|[Bool](/API_docs/types/Bool.html) | Optional|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|



### Type: [StoryView](/API_docs/types/StoryView.html)


### Example:

```
$storyView = ['_' => 'storyView', 'blocked' => Bool, 'blocked_my_stories_from' => Bool, 'user_id' => long, 'date' => int, 'reaction' => Reaction];
```  
