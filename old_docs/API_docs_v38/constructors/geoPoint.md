---
title: geoPoint
description: Geo point
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geoPoint  
[Back to constructors index](index.md)



Geo point

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|long|[double](../types/double.md) | Yes|Long|
|lat|[double](../types/double.md) | Yes|Lat|



### Type: [GeoPoint](../types/GeoPoint.md)


### Example:

```php
$geoPoint = ['_' => 'geoPoint', 'long' => double, 'lat' => double];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "geoPoint", "long": double, "lat": double}
```


Or, if you're into Lua:

```lua
geoPoint={_='geoPoint', long=double, lat=double}

```


