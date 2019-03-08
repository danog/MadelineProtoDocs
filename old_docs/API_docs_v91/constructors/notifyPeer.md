---
title: notifyPeer
description: Notify peer
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: notifyPeer  
[Back to constructors index](index.md)



Notify peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|



### Type: [NotifyPeer](../types/NotifyPeer.md)


### Example:

```php
$notifyPeer = ['_' => 'notifyPeer', 'peer' => Peer];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "notifyPeer", "peer": Peer}
```


Or, if you're into Lua:

```lua
notifyPeer={_='notifyPeer', peer=Peer}

```


