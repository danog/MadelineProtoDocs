---
title: "storyItemSkipped"
description: "storyItemSkipped attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyItemSkipped  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|close\_friends|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[int](/API_docs/types/int.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|expire\_date|[int](/API_docs/types/int.html) | Yes|



### Type: [StoryItem](/API_docs/types/StoryItem.html)


### Example:

```
$storyItemSkipped = ['_' => 'storyItemSkipped', 'close_friends' => Bool, 'id' => int, 'date' => int, 'expire_date' => int];
```  
