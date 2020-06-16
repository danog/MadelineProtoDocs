---
title: messageMediaGeo
description: Attached map.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGeo  
[Back to constructors index](index.md)



Attached map.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|GeoPoint|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaGeo = ['_' => 'messageMediaGeo', 'geo' => GeoPoint];
```  


Or, if you're into Lua:

```lua
messageMediaGeo={_='messageMediaGeo', geo=GeoPoint}

```


