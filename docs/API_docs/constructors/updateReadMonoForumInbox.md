---
title: "updateReadMonoForumInbox"
description: "updateReadMonoForumInbox attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadMonoForumInbox  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|channel\_id|[long](/API_docs/types/long.html) | Yes|
|saved\_peer\_id|[Peer](/API_docs/types/Peer.html) | Yes|
|read\_max\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateReadMonoForumInbox = ['_' => 'updateReadMonoForumInbox', 'channel_id' => long, 'saved_peer_id' => Peer, 'read_max_id' => int];
```  
