---
title: inputPeerChannel
description: Peer channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerChannel  
[Back to constructors index](index.md)



Peer channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channel\_id|[int](../types/int.md) | Yes|Channel ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputPeer](../types/InputPeer.md)


### Example:

```php
$inputPeerChannel = ['_' => 'inputPeerChannel', 'channel_id' => int, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPeerChannel", "channel_id": int, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputPeerChannel={_='inputPeerChannel', channel_id=int, access_hash=long}

```


