---
title: "storyViewPublicRepost"
description: "storyViewPublicRepost attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyViewPublicRepost  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|blocked|[Bool](/API_docs/types/Bool.html) | Optional|
|blocked\_my\_stories\_from|[Bool](/API_docs/types/Bool.html) | Optional|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Yes|



### Type: [StoryView](/API_docs/types/StoryView.html)


### Example:

```
$storyViewPublicRepost = ['_' => 'storyViewPublicRepost', 'blocked' => Bool, 'blocked_my_stories_from' => Bool, 'peer_id' => Peer, 'story' => StoryItem];
```  
