---
title: "keyboardButtonRequestPeer"
description: "keyboardButtonRequestPeer attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: keyboardButtonRequestPeer  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[string](/API_docs/types/string.html) | Yes|
|button\_id|[int](/API_docs/types/int.html) | Yes|
|peer\_type|[RequestPeerType](/API_docs/types/RequestPeerType.html) | Yes|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$keyboardButtonRequestPeer = ['_' => 'keyboardButtonRequestPeer', 'text' => 'string', 'button_id' => int, 'peer_type' => RequestPeerType];
```  
