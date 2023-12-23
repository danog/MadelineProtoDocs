---
title: "storyReaction"
description: "storyReaction attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyReaction  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|



### Type: [StoryReaction](/API_docs/types/StoryReaction.html)


### Example:

```
$storyReaction = ['_' => 'storyReaction', 'peer_id' => Peer, 'date' => int, 'reaction' => Reaction];
```  
