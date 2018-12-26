---
title: inputPeerForeign
description: Peer foreign
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerForeign  
[Back to constructors index](index.md)



Peer foreign

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputPeer](../types/InputPeer.md)


### Example:

```php
$inputPeerForeign = ['_' => 'inputPeerForeign', 'user_id' => int, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPeerForeign", "user_id": int, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputPeerForeign={_='inputPeerForeign', user_id=int, access_hash=long}

```


