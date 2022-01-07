---
title: "geoPoint"
description: "GeoPoint."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geoPoint  
[Back to constructors index](index.md)



GeoPoint.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|long|[double](../types/double.md) | Yes|Longtitude|
|lat|[double](../types/double.md) | Yes|Latitude|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|accuracy\_radius|[int](../types/int.md) | Optional|The estimated horizontal accuracy of the location, in meters; as defined by the sender.|



### Type: [GeoPoint](../types/GeoPoint.md)


### Example:

```php
$geoPoint = ['_' => 'geoPoint', 'long' => double, 'lat' => double, 'access_hash' => long, 'accuracy_radius' => int];
```  
