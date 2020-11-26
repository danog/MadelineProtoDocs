---
title: inputGeoPoint
description: Defines a GeoPoint by its coordinates.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGeoPoint  
[Back to constructors index](index.md)



Defines a GeoPoint by its coordinates.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lat|[double](../types/double.md) | Yes|Latitide|
|long|[double](../types/double.md) | Yes|Longtitude|
|accuracy\_radius|[int](../types/int.md) | Optional|



### Type: [InputGeoPoint](../types/InputGeoPoint.md)


### Example:

```php
$inputGeoPoint = ['_' => 'inputGeoPoint', 'lat' => double, 'long' => double, 'accuracy_radius' => int];
```  


Or, if you're into Lua:

```lua
inputGeoPoint={_='inputGeoPoint', lat=double, long=double, accuracy_radius=int}

```


