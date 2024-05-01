---
title: "inputWebFileGeoPointLocation"
description: "Used to download a server-generated image with the map preview from a geoPoint, see the webfile docs for more info »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebFileGeoPointLocation  
[Back to constructors index](/API_docs/constructors/index.html)



Used to download a server-generated image with the map preview from a [geoPoint](../constructors/geoPoint.html), see the [webfile docs for more info »](https://core.telegram.org/api/files#downloading-webfiles).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.html) | Optional|Generated from the `lat`, `long` and `accuracy_radius` parameters of the [geoPoint](../constructors/geoPoint.html)|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash of the [geoPoint](../constructors/geoPoint.html)|
|w|[int](/API_docs/types/int.html) | Yes|Map width in pixels before applying scale; 16-1024|
|h|[int](/API_docs/types/int.html) | Yes|Map height in pixels before applying scale; 16-1024|
|zoom|[int](/API_docs/types/int.html) | Yes|Map zoom level; 13-20|
|scale|[int](/API_docs/types/int.html) | Yes|Map scale; 1-3|



### Type: [InputWebFileLocation](/API_docs/types/InputWebFileLocation.html)


### Example:

```
$inputWebFileGeoPointLocation = ['_' => 'inputWebFileGeoPointLocation', 'geo_point' => InputGeoPoint, 'access_hash' => long, 'w' => int, 'h' => int, 'zoom' => int, 'scale' => int];
```  
