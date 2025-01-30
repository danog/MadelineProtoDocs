---
title: "messageReplyStoryHeader"
description: "Represents a reply to a story"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReplyStoryHeader  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a reply to a [story](https://core.telegram.org/api/stories)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Sender of the story.|
|story\_id|[int](/API_docs/types/int.html) | Yes|Story ID|



### Type: [MessageReplyHeader](/API_docs/types/MessageReplyHeader.html)


### Example:

```
$messageReplyStoryHeader = ['_' => 'messageReplyStoryHeader', 'peer' => long, 'story_id' => int];
```  
