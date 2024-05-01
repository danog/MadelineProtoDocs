---
title: "messageActionRequestedPeerSentMe"
description: "messageActionRequestedPeerSentMe attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionRequestedPeerSentMe  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|button\_id|[int](/API_docs/types/int.html) | Yes|
|peers|Array of [RequestedPeer](/API_docs/types/RequestedPeer.html) | Yes|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionRequestedPeerSentMe = ['_' => 'messageActionRequestedPeerSentMe', 'button_id' => int, 'peers' => [RequestedPeer, RequestedPeer]];
```  
