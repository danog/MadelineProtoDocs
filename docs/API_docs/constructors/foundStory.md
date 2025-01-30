---
title: "foundStory"
description: "A story found using global story search »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: foundStory  
[Back to constructors index](/API_docs/constructors/index.html)



A story found using [global story search »](https://core.telegram.org/api/stories#searching-stories).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The peer that posted the story.|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Yes|The story.|



### Type: [FoundStory](/API_docs/types/FoundStory.html)


### Example:

```
$foundStory = ['_' => 'foundStory', 'peer' => long, 'story' => StoryItem];
```  
