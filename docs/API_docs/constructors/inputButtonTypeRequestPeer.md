---
title: "inputButtonTypeRequestPeer"
description: "inputButtonTypeRequestPeer attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputButtonTypeRequestPeer  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|name\_requested|[Bool](/API_docs/types/Bool.html) | Optional|
|username\_requested|[Bool](/API_docs/types/Bool.html) | Optional|
|photo\_requested|[Bool](/API_docs/types/Bool.html) | Optional|
|button\_id|[int](/API_docs/types/int.html) | Yes|
|peer\_type|[RequestPeerType](/API_docs/types/RequestPeerType.html) | Yes|
|max\_quantity|[int](/API_docs/types/int.html) | Yes|



### Type: [ButtonType](/API_docs/types/ButtonType.html)


### Example:

```
$inputButtonTypeRequestPeer = ['_' => 'inputButtonTypeRequestPeer', 'name_requested' => Bool, 'username_requested' => Bool, 'photo_requested' => Bool, 'button_id' => int, 'peer_type' => RequestPeerType, 'max_quantity' => int];
```  
