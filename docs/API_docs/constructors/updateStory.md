---
title: "updateStory"
description: "A new story was posted."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateStory  
[Back to constructors index](/API_docs/constructors/index.html)



A new story was posted.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|ID of the poster.|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Yes|The story that was posted.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateStory = ['_' => 'updateStory', 'peer' => long, 'story' => StoryItem];
```  
