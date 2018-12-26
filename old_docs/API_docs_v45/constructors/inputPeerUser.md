---
title: inputPeerUser
description: Peer user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPeerUser  
[Back to constructors index](index.md)



Peer user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputPeer](../types/InputPeer.md)


### Example:

```php
$inputPeerUser = ['_' => 'inputPeerUser', 'user_id' => int, 'access_hash' => long];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputPeerUser", "user_id": int, "access_hash": long}
```


Or, if you're into Lua:

```lua
inputPeerUser={_='inputPeerUser', user_id=int, access_hash=long}

```


