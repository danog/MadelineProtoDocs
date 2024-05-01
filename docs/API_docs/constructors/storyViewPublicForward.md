---
title: "storyViewPublicForward"
description: "A certain peer has forwarded the story as a message to a public chat or channel."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyViewPublicForward  
[Back to constructors index](/API_docs/constructors/index.html)



A certain peer has forwarded the story as a message to a public chat or channel.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blocked|[Bool](/API_docs/types/Bool.html) | Optional|Whether we have [completely blocked](https://core.telegram.org/api/block) this user, including from viewing more of our stories.|
|blocked\_my\_stories\_from|[Bool](/API_docs/types/Bool.html) | Optional|Whether we have [blocked](https://core.telegram.org/api/block) this user from viewing more of our stories.|
|message|[Message](/API_docs/types/Message.html) | Optional|The message with the forwarded story.|



### Type: [StoryView](/API_docs/types/StoryView.html)


### Example:

```
$storyViewPublicForward = ['_' => 'storyViewPublicForward', 'blocked' => Bool, 'blocked_my_stories_from' => Bool, 'message' => Message];
```  
