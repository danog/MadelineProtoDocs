---
title: "messageEmpty"
description: "Empty constructor, non-existent message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEmpty  
[Back to constructors index](index.md)



Empty constructor, non-existent message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|Message identifier|
|peer\_id|[Peer](../types/Peer.md) | Optional|



### Type: [Message](../types/Message.md)


### Example:

```php
$messageEmpty = ['_' => 'messageEmpty', 'id' => int, 'peer_id' => Peer];
```  


Or, if you're into Lua:

```lua
messageEmpty={_='messageEmpty', id=int, peer_id=Peer}

```


