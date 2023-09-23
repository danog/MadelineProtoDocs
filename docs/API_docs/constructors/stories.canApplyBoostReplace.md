---
title: "stories.canApplyBoostReplace"
description: "stories.canApplyBoostReplace attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_canApplyBoostReplace.html
---
# Constructor: stories.canApplyBoostReplace  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|current\_boost|[Peer](/API_docs/types/Peer.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|



### Type: [stories.CanApplyBoostResult](/API_docs/types/stories.CanApplyBoostResult.html)


### Example:

```
$stories_canApplyBoostReplace = ['_' => 'stories.canApplyBoostReplace', 'current_boost' => Peer, 'chats' => [Chat, Chat]];
```  
