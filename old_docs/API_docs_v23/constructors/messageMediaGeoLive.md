---
title: messageMediaGeoLive
description: Indicates a [live geolocation](https://core.telegram.org/api/live-location)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGeoLive  
[Back to constructors index](index.md)



Indicates a [live geolocation](https://core.telegram.org/api/live-location)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geolocation|
|period|[int](../types/int.md) | Yes|Validity period of provided geolocation|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaGeoLive = ['_' => 'messageMediaGeoLive', 'geo' => GeoPoint, 'period' => int];
```  


Or, if you're into Lua:

```lua
messageMediaGeoLive={_='messageMediaGeoLive', geo=GeoPoint, period=int}

```


