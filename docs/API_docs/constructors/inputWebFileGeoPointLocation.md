---
title: "inputWebFileGeoPointLocation"
description: "Geolocation"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebFileGeoPointLocation  
[Back to constructors index](/API_docs/constructors/index.html)



Geolocation

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.html) | Optional|Geolocation|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|w|[int](/API_docs/types/int.html) | Yes|Map width in pixels before applying scale; 16-1024|
|h|[int](/API_docs/types/int.html) | Yes|Map height in pixels before applying scale; 16-1024|
|zoom|[int](/API_docs/types/int.html) | Yes|Map zoom level; 13-20|
|scale|[int](/API_docs/types/int.html) | Yes|Map scale; 1-3|



### Type: [InputWebFileLocation](/API_docs/types/InputWebFileLocation.html)


### Example:

```
$inputWebFileGeoPointLocation = ['_' => 'inputWebFileGeoPointLocation', 'geo_point' => InputGeoPoint, 'access_hash' => long, 'w' => int, 'h' => int, 'zoom' => int, 'scale' => int];
```  
