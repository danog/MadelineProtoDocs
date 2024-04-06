---
title: "inputKeyboardButtonRequestPeer"
description: "inputKeyboardButtonRequestPeer attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputKeyboardButtonRequestPeer  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|name\_requested|[Bool](/API_docs/types/Bool.html) | Optional|
|username\_requested|[Bool](/API_docs/types/Bool.html) | Optional|
|photo\_requested|[Bool](/API_docs/types/Bool.html) | Optional|
|text|[string](/API_docs/types/string.html) | Yes|
|button\_id|[int](/API_docs/types/int.html) | Yes|
|peer\_type|[RequestPeerType](/API_docs/types/RequestPeerType.html) | Yes|
|max\_quantity|[int](/API_docs/types/int.html) | Yes|



### Type: [KeyboardButton](/API_docs/types/KeyboardButton.html)


### Example:

```
$inputKeyboardButtonRequestPeer = ['_' => 'inputKeyboardButtonRequestPeer', 'name_requested' => Bool, 'username_requested' => Bool, 'photo_requested' => Bool, 'text' => 'string', 'button_id' => int, 'peer_type' => RequestPeerType, 'max_quantity' => int];
```  
