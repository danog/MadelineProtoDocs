---
title: "updateMessageExtendedMedia"
description: "Extended media update"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateMessageExtendedMedia  
[Back to constructors index](/API_docs/constructors/index.html)



Extended media update

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|Peer|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID|
|extended\_media|[MessageExtendedMedia](/API_docs/types/MessageExtendedMedia.html) | Yes|Extended media|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateMessageExtendedMedia = ['_' => 'updateMessageExtendedMedia', 'peer' => Peer, 'msg_id' => int, 'extended_media' => MessageExtendedMedia];
```  
