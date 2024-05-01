---
title: "requestedPeerUser"
description: "requestedPeerUser attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requestedPeerUser  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[long](/API_docs/types/long.html) | Yes|
|first\_name|[string](/API_docs/types/string.html) | Optional|
|last\_name|[string](/API_docs/types/string.html) | Optional|
|username|[string](/API_docs/types/string.html) | Optional|
|photo|[Photo](/API_docs/types/Photo.html) | Optional|



### Type: [RequestedPeer](/API_docs/types/RequestedPeer.html)


### Example:

```
$requestedPeerUser = ['_' => 'requestedPeerUser', 'user_id' => long, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string', 'photo' => Photo];
```  
