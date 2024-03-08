---
title: "messageMediaStory"
description: "Represents a forwarded story or a story mention."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaStory  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a forwarded [story](https://core.telegram.org/api/stories) or a story mention.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|via\_mention|[Bool](/API_docs/types/Bool.html) | Optional|If set, indicates that this someone has mentioned us in this story (i.e. by tagging us in the description) or vice versa, we have mentioned the other peer (if the message is outgoing).|
|peer|[long](/API_docs/types/long.html) | Yes|Peer that posted the story.|
|id|[int](/API_docs/types/int.html) | Yes|Story ID|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Optional|The story itself, if absent fetch it using [stories.getStoriesByID](../methods/stories.getStoriesByID.html) and the `peer`/`id` parameters specified above.|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaStory = ['_' => 'messageMediaStory', 'via_mention' => Bool, 'peer' => long, 'id' => int, 'story' => StoryItem];
```  
