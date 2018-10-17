---
title: topPeer
description: topPeer attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: topPeer  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](../types/Peer.md) | Yes|
|rating|[double](../types/double.md) | Yes|



### Type: [TopPeer](../types/TopPeer.md)


### Example:

```php
$topPeer = ['_' => 'topPeer', 'peer' => Peer, 'rating' => double];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "topPeer", "peer": Peer, "rating": double}
```


Or, if you're into Lua:

```lua
topPeer={_='topPeer', peer=Peer, rating=double}

```


