---
title: "buttonTypeRequestPeer"
description: "buttonTypeRequestPeer attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: buttonTypeRequestPeer  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|button\_id|[int](/API_docs/types/int.html) | Yes|
|peer\_type|[RequestPeerType](/API_docs/types/RequestPeerType.html) | Yes|
|max\_quantity|[int](/API_docs/types/int.html) | Yes|



### Type: [ButtonType](/API_docs/types/ButtonType.html)


### Example:

```
$buttonTypeRequestPeer = ['_' => 'buttonTypeRequestPeer', 'button_id' => int, 'peer_type' => RequestPeerType, 'max_quantity' => int];
```  
