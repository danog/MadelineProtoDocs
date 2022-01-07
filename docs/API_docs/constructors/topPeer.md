---
title: "topPeer"
description: "Top peer"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: topPeer  
[Back to constructors index](index.md)



Top peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|rating|[double](../types/double.md) | Yes|Rating as computed in [top peer rating »](https://core.telegram.org/api/top-rating)|



### Type: [TopPeer](../types/TopPeer.md)


### Example:

```php
$topPeer = ['_' => 'topPeer', 'peer' => Peer, 'rating' => double];
```  
