---
title: peerChannel
description: Peer channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerChannel  
[Back to constructors index](index.md)



Peer channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|



### Type: [Peer](../types/Peer.md)


### Example:

```php
$peerChannel = ['_' => 'peerChannel', 'channel_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "peerChannel", "channel_id": int}
```


Or, if you're into Lua:

```lua
peerChannel={_='peerChannel', channel_id=int}

```


