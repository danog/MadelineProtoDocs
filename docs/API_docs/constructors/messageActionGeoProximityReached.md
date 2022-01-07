---
title: "messageActionGeoProximityReached"
description: "A user of the chat is now in proximity of another user"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGeoProximityReached  
[Back to constructors index](index.md)



A user of the chat is now in proximity of another user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|from\_id|[Peer](../types/Peer.md) | Yes|The user or chat that is now in proximity of `to_id`|
|to\_id|[Peer](../types/Peer.md) | Yes|The user or chat that subscribed to [live geolocation proximity alerts](https://core.telegram.org/api/live-location#proximity-alert)|
|distance|[int](../types/int.md) | Yes|Distance, in meters (0-100000)|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionGeoProximityReached = ['_' => 'messageActionGeoProximityReached', 'from_id' => Peer, 'to_id' => Peer, 'distance' => int];
```  
