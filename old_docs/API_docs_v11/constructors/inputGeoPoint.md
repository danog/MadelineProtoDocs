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
|latitude|[double](../types/double.md) | Yes|
|longitude|[double](../types/double.md) | Yes|



### Type: [InputGeoPoint](../types/InputGeoPoint.md)


### Example:

```php
$inputGeoPoint = ['_' => 'inputGeoPoint', 'latitude' => double, 'longitude' => double];
```  


Or, if you're into Lua:

```lua
inputGeoPoint={_='inputGeoPoint', latitude=double, longitude=double}

```


