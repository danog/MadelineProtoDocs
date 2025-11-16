---
title: "storyItemSkipped"
description: "Represents an active story, whose full information was omitted for space and performance reasons; use stories.getStoriesByID to fetch full info about the skipped story when and if needed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyItemSkipped  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an active story, whose full information was omitted for space and performance reasons; use [stories.getStoriesByID](../methods/stories.getStoriesByID.html) to fetch full info about the skipped story when and if needed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|close\_friends|[Bool](/API_docs/types/Bool.html) | Optional|Whether this story can only be viewed by [our close friends, see here »](https://core.telegram.org/api/privacy) for more info|
|live|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[int](/API_docs/types/int.html) | Yes|Story ID|
|date|[int](/API_docs/types/int.html) | Yes|When was the story posted.|
|expire\_date|[int](/API_docs/types/int.html) | Yes|When does the story expire.|



### Type: [StoryItem](/API_docs/types/StoryItem.html)


### Example:

```
$storyItemSkipped = ['_' => 'storyItemSkipped', 'close_friends' => Bool, 'live' => Bool, 'id' => int, 'date' => int, 'expire_date' => int];
```  
