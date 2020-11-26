---
title: messageMediaGeoLive
description: Indicates a live geolocation
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGeoLive  
[Back to constructors index](index.md)



Indicates a live geolocation

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geolocation|
|heading|[int](../types/int.md) | Optional|
|period|[int](../types/int.md) | Yes|Validity period of provided geolocation|
|proximity\_notification\_radius|[int](../types/int.md) | Optional|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaGeoLive = ['_' => 'messageMediaGeoLive', 'geo' => GeoPoint, 'heading' => int, 'period' => int, 'proximity_notification_radius' => int];
```  


Or, if you're into Lua:

```lua
messageMediaGeoLive={_='messageMediaGeoLive', geo=GeoPoint, heading=int, period=int, proximity_notification_radius=int}

```


