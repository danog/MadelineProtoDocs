---
title: "storyReaction"
description: "How a certain peer reacted to a story"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyReaction  
[Back to constructors index](/API_docs/constructors/index.html)



How a certain peer reacted to a story

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|The peer|
|date|[int](/API_docs/types/int.html) | Yes|Reaction date|
|reaction|[Reaction](/API_docs/types/Reaction.html) | Optional|The reaction|



### Type: [StoryReaction](/API_docs/types/StoryReaction.html)


### Example:

```
$storyReaction = ['_' => 'storyReaction', 'peer_id' => Peer, 'date' => int, 'reaction' => Reaction];
```  
