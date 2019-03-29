---
title: updateReadChannelInbox
description: Update read channel inbox
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateReadChannelInbox  
[Back to constructors index](index.md)



Update read channel inbox

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|Peer|
|max\_id|[int](../types/int.md) | Yes|Max ID|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateReadChannelInbox = ['_' => 'updateReadChannelInbox', 'peer' => Peer, 'max_id' => int];
```  


Or, if you're into Lua:

```lua
updateReadChannelInbox={_='updateReadChannelInbox', peer=Peer, max_id=int}

```


