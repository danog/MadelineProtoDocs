---
title: "inputWebFileGeoPointLocation"
description: "Geolocation"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebFileGeoPointLocation  
[Back to constructors index](index.md)



Geolocation

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geolocation|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|w|[int](../types/int.md) | Yes|Map width in pixels before applying scale; 16-1024|
|h|[int](../types/int.md) | Yes|Map height in pixels before applying scale; 16-1024|
|zoom|[int](../types/int.md) | Yes|Map zoom level; 13-20|
|scale|[int](../types/int.md) | Yes|Map scale; 1-3|



### Type: [InputWebFileLocation](../types/InputWebFileLocation.md)


### Example:

```php
$inputWebFileGeoPointLocation = ['_' => 'inputWebFileGeoPointLocation', 'geo_point' => InputGeoPoint, 'access_hash' => long, 'w' => int, 'h' => int, 'zoom' => int, 'scale' => int];
```  
