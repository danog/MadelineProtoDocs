---
title: "inputMediaGeoLive"
description: "Live geolocation"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaGeoLive  
[Back to constructors index](/API_docs/constructors/index.html)



[Live geolocation](https://core.telegram.org/api/live-location)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stopped|[Bool](/API_docs/types/Bool.html) | Optional|Whether sending of the geolocation was stopped|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.html) | Optional|Current geolocation|
|heading|[int](/API_docs/types/int.html) | Optional|For [live locations](https://core.telegram.org/api/live-location), a direction in which the location moves, in degrees; 1-360.|
|period|[int](/API_docs/types/int.html) | Optional|Validity period of the current location|
|proximity\_notification\_radius|[int](/API_docs/types/int.html) | Optional|For [live locations](https://core.telegram.org/api/live-location), a maximum distance to another chat member for proximity alerts, in meters (0-100000)|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaGeoLive = ['_' => 'inputMediaGeoLive', 'stopped' => Bool, 'geo_point' => InputGeoPoint, 'heading' => int, 'period' => int, 'proximity_notification_radius' => int];
```  
