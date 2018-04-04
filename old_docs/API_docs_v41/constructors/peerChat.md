---
title: peerChat
description: peerChat attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerChat  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|chat\_id|[int](../types/int.md) | Yes|



### Type: [Peer](../types/Peer.md)


### Example:

```
$peerChat = ['_' => 'peerChat', 'chat_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "peerChat", "chat_id": int}
```


Or, if you're into Lua:  


```
peerChat={_='peerChat', chat_id=int}

```


