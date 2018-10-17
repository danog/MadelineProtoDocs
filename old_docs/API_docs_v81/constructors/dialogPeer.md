---
title: dialogPeer
description: dialogPeer attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogPeer  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](../types/Peer.md) | Yes|



### Type: [DialogPeer](../types/DialogPeer.md)


### Example:

```php
$dialogPeer = ['_' => 'dialogPeer', 'peer' => Peer];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "dialogPeer", "peer": Peer}
```


Or, if you're into Lua:

```lua
dialogPeer={_='dialogPeer', peer=Peer}

```


