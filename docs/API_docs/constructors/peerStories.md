---
title: "peerStories"
description: "Stories associated to a peer"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerStories  
[Back to constructors index](/API_docs/constructors/index.html)



[Stories](https://core.telegram.org/api/stories) associated to a peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The peer|
|max\_read\_id|[int](/API_docs/types/int.html) | Optional|If set, contains the ID of the maximum read story|
|stories|Array of [StoryItem](/API_docs/types/StoryItem.html) | Yes|Stories|



### Type: [PeerStories](/API_docs/types/PeerStories.html)


### Example:

```
$peerStories = ['_' => 'peerStories', 'peer' => long, 'max_read_id' => int, 'stories' => [StoryItem, StoryItem]];
```  
