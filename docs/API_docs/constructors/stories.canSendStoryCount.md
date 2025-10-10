---
title: "stories.canSendStoryCount"
description: "Contains the number of available active story slots (equal to the value of the story_expiring_limit_* client configuration parameter minus the number of currently active stories)."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_canSendStoryCount.html
---
# Constructor: stories.canSendStoryCount  
[Back to constructors index](/API_docs/constructors/index.html)



Contains the number of available active story slots (equal to the value of the [`story_expiring_limit_*` client configuration parameter](https://core.telegram.org/api/config#story-expiring-limit-default) minus the number of currently active stories).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count\_remains|[int](/API_docs/types/int.html) | Yes|Remaining active story slots.|



### Type: [stories.CanSendStoryCount](/API_docs/types/stories.CanSendStoryCount.html)


### Example:

```
$stories_canSendStoryCount = ['_' => 'stories.canSendStoryCount', 'count_remains' => int];
```  
