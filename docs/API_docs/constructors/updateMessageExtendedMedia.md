---
title: "updateMessageExtendedMedia"
description: "updateMessageExtendedMedia attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageExtendedMedia  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|extended\_media|[MessageExtendedMedia](/API_docs/types/MessageExtendedMedia.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessageExtendedMedia = ['_' => 'updateMessageExtendedMedia', 'peer' => Peer, 'msg_id' => int, 'extended_media' => MessageExtendedMedia];
```  
