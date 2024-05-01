---
title: "messageMediaGeoLive"
description: "Indicates a live geolocation"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGeoLive  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates a [live geolocation](https://core.telegram.org/api/live-location)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|Geolocation|
|heading|[int](/API_docs/types/int.html) | Optional|For [live locations](https://core.telegram.org/api/live-location), a direction in which the location moves, in degrees; 1-360|
|period|[int](/API_docs/types/int.html) | Yes|Validity period of provided geolocation|
|proximity\_notification\_radius|[int](/API_docs/types/int.html) | Optional|For [live locations](https://core.telegram.org/api/live-location), a maximum distance to another chat member for proximity alerts, in meters (0-100000).|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaGeoLive = ['_' => 'messageMediaGeoLive', 'geo' => GeoPoint, 'heading' => int, 'period' => int, 'proximity_notification_radius' => int];
```  
