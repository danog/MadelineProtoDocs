---
title: "communities.peerLinkRequests"
description: "communities.peerLinkRequests attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/communities_peerLinkRequests.html
---
# Constructor: communities.peerLinkRequests  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|total\_count|[int](/API_docs/types/int.html) | Yes|
|requests|Array of [CommunityPeerRequest](/API_docs/types/CommunityPeerRequest.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [communities.PeerLinkRequests](/API_docs/types/communities.PeerLinkRequests.html)


### Example:

```
$communities_peerLinkRequests = ['_' => 'communities.peerLinkRequests', 'total_count' => int, 'requests' => [CommunityPeerRequest, CommunityPeerRequest], 'next_offset' => 'string', 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
