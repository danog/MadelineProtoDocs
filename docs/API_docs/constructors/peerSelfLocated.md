---
title: "peerSelfLocated"
description: "Current peer"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerSelfLocated  
[Back to constructors index](/API_docs/constructors/index.md)



Current peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](/API_docs/types/int.md) | Yes|Expiry of geolocation info for current peer|



### Type: [PeerLocated](/API_docs/types/PeerLocated.md)


### Example:

```php
$peerSelfLocated = ['_' => 'peerSelfLocated', 'expires' => int];
```  
