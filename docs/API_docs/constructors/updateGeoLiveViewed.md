---
title: "updateGeoLiveViewed"
description: "Live geoposition message was viewed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGeoLiveViewed  
[Back to constructors index](index.md)



Live geoposition message was viewed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[Peer](../types/Peer.md) | Yes|The user that viewed the live geoposition|
|msg\_id|[int](../types/int.md) | Yes|Message ID of geoposition message|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateGeoLiveViewed = ['_' => 'updateGeoLiveViewed', 'peer' => Peer, 'msg_id' => int];
```  


Or, if you're into Lua:

```lua
updateGeoLiveViewed={_='updateGeoLiveViewed', peer=Peer, msg_id=int}

```


