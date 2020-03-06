---
title: updateGeoLiveViewed
description: updateGeoLiveViewed attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGeoLiveViewed  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[Peer](../types/Peer.md) | Yes|
|msg\_id|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateGeoLiveViewed = ['_' => 'updateGeoLiveViewed', 'peer' => Peer, 'msg_id' => int];
```  


Or, if you're into Lua:

```lua
updateGeoLiveViewed={_='updateGeoLiveViewed', peer=Peer, msg_id=int}

```


