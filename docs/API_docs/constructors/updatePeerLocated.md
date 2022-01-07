---
title: "updatePeerLocated"
description: "List of peers near you was updated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerLocated  
[Back to constructors index](index.md)



List of peers near you was updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peers|Array of [PeerLocated](../types/PeerLocated.md) | Yes|Geolocated peer list update|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePeerLocated = ['_' => 'updatePeerLocated', 'peers' => [PeerLocated, PeerLocated]];
```  
