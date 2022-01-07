---
title: "updatePeerLocated"
description: "List of peers near you was updated"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerLocated  
[Back to constructors index](/API_docs/constructors/index.md)



List of peers near you was updated

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peers|Array of [PeerLocated](/API_docs/types/PeerLocated.md) | Yes|Geolocated peer list update|



### Type: [Update](/API_docs/types/Update.md)


### Example:

```php
$updatePeerLocated = ['_' => 'updatePeerLocated', 'peers' => [PeerLocated, PeerLocated]];
```  
