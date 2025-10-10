---
title: "updateGroupCallMessage"
description: "updateGroupCallMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCallMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|from\_id|[Peer](/API_docs/types/Peer.html) | Yes|
|message|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGroupCallMessage = ['_' => 'updateGroupCallMessage', 'call' => InputGroupCall, 'from_id' => Peer, 'message' => TextWithEntities];
```  
