---
title: "stories.peerStories"
description: "stories.peerStories attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_peerStories.html
---
# Constructor: stories.peerStories  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|stories|[PeerStories](/API_docs/types/PeerStories.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [stories.PeerStories](/API_docs/types/stories.PeerStories.html)


### Example:

```
$stories_peerStories = ['_' => 'stories.peerStories', 'stories' => PeerStories, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
