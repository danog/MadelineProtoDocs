---
title: notifyPeer
description: notifyPeer attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: notifyPeer  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](../types/Peer.md) | Yes|



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


