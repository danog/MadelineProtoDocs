---
title: "communityFull"
description: "communityFull attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: communityFull  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](/API_docs/types/long.html) | Yes|
|about|[string](/API_docs/types/string.html) | Yes|
|chat\_photo|[Photo](/API_docs/types/Photo.html) | Optional|
|linked\_peers|Array of [CommunityPeer](/API_docs/types/CommunityPeer.html) | Yes|
|admins\_count|[int](/API_docs/types/int.html) | Optional|
|kicked\_count|[int](/API_docs/types/int.html) | Optional|
|peer\_link\_requests\_pending|[int](/API_docs/types/int.html) | Optional|



### Type: [ChatFull](/API_docs/types/ChatFull.html)


### Example:

```
$communityFull = ['_' => 'communityFull', 'id' => long, 'about' => 'string', 'chat_photo' => Photo, 'linked_peers' => [CommunityPeer, CommunityPeer], 'admins_count' => int, 'kicked_count' => int, 'peer_link_requests_pending' => int];
```  
