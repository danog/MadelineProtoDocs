---
title: "notifyForumTopic"
description: "notifyForumTopic attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: notifyForumTopic  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|
|top\_msg\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [NotifyPeer](/API_docs/types/NotifyPeer.html)


### Example:

```
$notifyForumTopic = ['_' => 'notifyForumTopic', 'peer' => Peer, 'top_msg_id' => int];
```  
