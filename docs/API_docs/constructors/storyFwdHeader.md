---
title: "storyFwdHeader"
description: "Contains info about the original poster of a reposted story."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyFwdHeader  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about the original poster of a reposted story.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|modified|[Bool](/API_docs/types/Bool.html) | Optional|Whether the story media was modified before reposting it (for example by overlaying a round video with a reaction).|
|from|[Peer](/API_docs/types/Peer.html) | Optional|Peer that originally posted the story; will be empty for stories forwarded from a user with forwards privacy enabled, in which case `from_name` will be set, instead.|
|from\_name|[string](/API_docs/types/string.html) | Optional|Will be set for stories forwarded from a user with forwards privacy enabled, in which case `from` will also be empty.|
|story\_id|[int](/API_docs/types/int.html) | Optional|, contains the story ID|



### Type: [StoryFwdHeader](/API_docs/types/StoryFwdHeader.html)


### Example:

```
$storyFwdHeader = ['_' => 'storyFwdHeader', 'modified' => Bool, 'from' => Peer, 'from_name' => 'string', 'story_id' => int];
```  
