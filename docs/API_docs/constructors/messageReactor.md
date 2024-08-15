---
title: "messageReactor"
description: "messageReactor attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageReactor  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|top|[Bool](/API_docs/types/Bool.html) | Optional|
|my|[Bool](/API_docs/types/Bool.html) | Optional|
|anonymous|[Bool](/API_docs/types/Bool.html) | Optional|
|peer\_id|[Peer](/API_docs/types/Peer.html) | Optional|
|count|[int](/API_docs/types/int.html) | Yes|



### Type: [MessageReactor](/API_docs/types/MessageReactor.html)


### Example:

```
$messageReactor = ['_' => 'messageReactor', 'top' => Bool, 'my' => Bool, 'anonymous' => Bool, 'peer_id' => Peer, 'count' => int];
```  
