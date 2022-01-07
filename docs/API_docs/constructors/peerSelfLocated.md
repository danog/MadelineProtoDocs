---
title: "peerSelfLocated"
description: "Current peer"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerSelfLocated  
[Back to constructors index](index.md)



Current peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|expires|[int](../types/int.md) | Yes|Expiry of geolocation info for current peer|



### Type: [PeerLocated](../types/PeerLocated.md)


### Example:

```php
$peerSelfLocated = ['_' => 'peerSelfLocated', 'expires' => int];
```  
