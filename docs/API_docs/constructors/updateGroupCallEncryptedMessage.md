---
title: "updateGroupCallEncryptedMessage"
description: "updateGroupCallEncryptedMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCallEncryptedMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|from\_id|[Peer](/API_docs/types/Peer.html) | Yes|
|encrypted\_message|[bytes](/API_docs/types/bytes.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGroupCallEncryptedMessage = ['_' => 'updateGroupCallEncryptedMessage', 'call' => InputGroupCall, 'from_id' => Peer, 'encrypted_message' => 'bytes'];
```  
