---
title: "storyReactionPublicRepost"
description: "A certain peer has reposted the story."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyReactionPublicRepost  
[Back to constructors index](/API_docs/constructors/index.html)



A certain peer has reposted the story.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|The peer that reposted the story.|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Yes|The reposted story.|



### Type: [StoryReaction](/API_docs/types/StoryReaction.html)


### Example:

```
$storyReactionPublicRepost = ['_' => 'storyReactionPublicRepost', 'peer_id' => Peer, 'story' => StoryItem];
```  
