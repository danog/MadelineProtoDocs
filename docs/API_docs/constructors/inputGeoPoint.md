---
title: "inputGeoPoint"
description: "Defines a GeoPoint by its coordinates."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGeoPoint  
[Back to constructors index](/API_docs/constructors/index.html)



Defines a GeoPoint by its coordinates.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lat|[double](/API_docs/types/double.html) | Yes|Latitude|
|long|[double](/API_docs/types/double.html) | Yes|Longitude|
|accuracy\_radius|[int](/API_docs/types/int.html) | Optional|The estimated horizontal accuracy of the location, in meters; as defined by the sender.|



### Type: [InputGeoPoint](/API_docs/types/InputGeoPoint.html)


### Example:

```
$inputGeoPoint = ['_' => 'inputGeoPoint', 'lat' => double, 'long' => double, 'accuracy_radius' => int];
```  
