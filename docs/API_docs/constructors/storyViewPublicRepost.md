---
title: "storyViewPublicRepost"
description: "A certain peer has reposted the story."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyViewPublicRepost  
[Back to constructors index](/API_docs/constructors/index.html)



A certain peer has reposted the story.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|[Bool](/API_docs/types/Bool.html) | Optional|Whether we have [completely blocked](https://core.telegram.org/api/block) this user, including from viewing more of our stories.|
|blocked\_my\_stories\_from|[Bool](/API_docs/types/Bool.html) | Optional|Whether we have [blocked](https://core.telegram.org/api/block) this user from viewing more of our stories.|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|The peer that reposted the story.|
|story|[StoryItem](/API_docs/types/StoryItem.html) | Yes|The reposted story.|



### Type: [StoryView](/API_docs/types/StoryView.html)


### Example:

```
$storyViewPublicRepost = ['_' => 'storyViewPublicRepost', 'blocked' => Bool, 'blocked_my_stories_from' => Bool, 'peer_id' => Peer, 'story' => StoryItem];
```  
