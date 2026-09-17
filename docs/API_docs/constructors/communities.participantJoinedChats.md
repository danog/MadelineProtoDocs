---
title: "communities.participantJoinedChats"
description: "communities.participantJoinedChats attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/communities_participantJoinedChats.html
---
# Constructor: communities.participantJoinedChats  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|creator\_chat\_ids|Array of [long](/API_docs/types/long.html) | Yes|
|joined\_chat\_ids|Array of [long](/API_docs/types/long.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [communities.ParticipantJoinedChats](/API_docs/types/communities.ParticipantJoinedChats.html)


### Example:

```
$communities_participantJoinedChats = ['_' => 'communities.participantJoinedChats', 'creator_chat_ids' => [long, long], 'joined_chat_ids' => [long, long], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
