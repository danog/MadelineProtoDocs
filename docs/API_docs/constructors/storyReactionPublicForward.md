---
title: "storyReactionPublicForward"
description: "A certain peer has forwarded the story as a message to a public chat or channel."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyReactionPublicForward  
[Back to constructors index](/API_docs/constructors/index.html)



A certain peer has forwarded the story as a message to a public chat or channel.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](/API_docs/types/Message.html) | Optional|The message with the forwarded story.|



### Type: [StoryReaction](/API_docs/types/StoryReaction.html)


### Example:

```
$storyReactionPublicForward = ['_' => 'storyReactionPublicForward', 'message' => Message];
```  
