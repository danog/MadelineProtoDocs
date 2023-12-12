---
title: "peerLocated"
description: "Peer geolocated nearby"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerLocated  
[Back to constructors index](/API_docs/constructors/index.html)



Peer geolocated nearby

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|
|expires|[int](/API_docs/types/int.html) | Yes|Validity period of current data|
|distance|[int](/API_docs/types/int.html) | Yes|Distance from the peer in meters|



### Type: [PeerLocated](/API_docs/types/PeerLocated.html)


### Example:

```
$peerLocated = ['_' => 'peerLocated', 'peer' => long, 'expires' => int, 'distance' => int];
```  
