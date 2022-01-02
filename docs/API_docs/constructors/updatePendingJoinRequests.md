---
title: "updatePendingJoinRequests"
description: "updatePendingJoinRequests attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePendingJoinRequests  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](../types/Peer.md) | Yes|
|requests\_pending|[int](../types/int.md) | Yes|
|recent\_requesters|Array of [long](../types/long.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePendingJoinRequests = ['_' => 'updatePendingJoinRequests', 'peer' => Peer, 'requests_pending' => int, 'recent_requesters' => [long, long]];
```  


Or, if you're into Lua:

```lua
updatePendingJoinRequests={_='updatePendingJoinRequests', peer=Peer, requests_pending=int, recent_requesters={long}}

```


