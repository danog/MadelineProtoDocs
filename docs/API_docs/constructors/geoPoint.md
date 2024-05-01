---
title: "geoPoint"
description: "GeoPoint."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geoPoint  
[Back to constructors index](/API_docs/constructors/index.html)



GeoPoint.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|long|[double](/API_docs/types/double.html) | Yes|Longitude|
|lat|[double](/API_docs/types/double.html) | Yes|Latitude|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|accuracy\_radius|[int](/API_docs/types/int.html) | Optional|The estimated horizontal accuracy of the location, in meters; as defined by the sender.|



### Type: [GeoPoint](/API_docs/types/GeoPoint.html)


### Example:

```
$geoPoint = ['_' => 'geoPoint', 'long' => double, 'lat' => double, 'access_hash' => long, 'accuracy_radius' => int];
```  
