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
|heading|[int](../types/int.md) | Optional|For [live locations](https://core.telegram.org/api/live-location), a direction in which the location moves, in degrees; 1-360|
|period|[int](../types/int.md) | Yes|Validity period of provided geolocation|
|proximity\_notification\_radius|[int](../types/int.md) | Optional|For [live locations](https://core.telegram.org/api/live-location), a maximum distance to another chat member for proximity alerts, in meters (0-100000).|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaGeoLive = ['_' => 'messageMediaGeoLive', 'geo' => GeoPoint, 'heading' => int, 'period' => int, 'proximity_notification_radius' => int];
```  


Or, if you're into Lua:

```lua
messageMediaGeoLive={_='messageMediaGeoLive', geo=GeoPoint, heading=int, period=int, proximity_notification_radius=int}

```


