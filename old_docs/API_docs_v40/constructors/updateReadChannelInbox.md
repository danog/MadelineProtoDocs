---
title: updateReadChannelInbox
description: Incoming messages in a [channel/supergroup](https://core.telegram.org/api/channel) were read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelInbox  
[Back to constructors index](index.md)



Incoming messages in a [channel/supergroup](https://core.telegram.org/api/channel) were read

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|max\_id|[int](../types/int.md) | Yes|Position up to which all incoming messages are read.|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelInbox = ['_' => 'updateReadChannelInbox', 'peer' => Peer, 'max_id' => int];
```  


Or, if you're into Lua:

```lua
updateReadChannelInbox={_='updateReadChannelInbox', peer=Peer, max_id=int}

```


