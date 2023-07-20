---
title: "messageMediaStory"
description: "messageMediaStory attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaStory  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|via\_mention|[Bool](/API_docs/types/Bool.html) | Optional|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|id|[int](/API_docs/types/int.html) | Yes|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Optional|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaStory = ['_' => 'messageMediaStory', 'via_mention' => Bool, 'user_id' => long, 'id' => int, 'story' => StoryItem];
```  
