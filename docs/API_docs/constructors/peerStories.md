---
title: "peerStories"
description: "peerStories attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerStories  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[long](/API_docs/types/long.html) | Yes|
|max\_read\_id|[int](/API_docs/types/int.html) | Optional|
|stories|Array of [StoryItem](/API_docs/types/StoryItem.html) | Yes|



### Type: [PeerStories](/API_docs/types/PeerStories.html)


### Example:

```
$peerStories = ['_' => 'peerStories', 'peer' => long, 'max_read_id' => int, 'stories' => [StoryItem, StoryItem]];
```  
