---
title: "updateGeoLiveViewed"
description: "Live geoposition message was viewed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGeoLiveViewed  
[Back to constructors index](/API_docs/constructors/index.html)



Live geoposition message was viewed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|The user that viewed the live geoposition|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID of geoposition message|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGeoLiveViewed = ['_' => 'updateGeoLiveViewed', 'peer' => Peer, 'msg_id' => int];
```  
