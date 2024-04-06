---
title: "requestedPeerChat"
description: "requestedPeerChat attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requestedPeerChat  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|
|title|[string](/API_docs/types/string.html) | Optional|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|



### Type: [RequestedPeer](/API_docs/types/RequestedPeer.html)


### Example:

```
$requestedPeerChat = ['_' => 'requestedPeerChat', 'chat_id' => long, 'title' => 'string', 'photo' => Photo];
```  
