---
title: inputGeoPoint
description: Geo point
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGeoPoint  
[Back to constructors index](index.md)



Geo point

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|latitude|[double](../types/double.md) | Yes|Latitude|
|longitude|[double](../types/double.md) | Yes|Longitude|



### Type: [InputGeoPoint](../types/InputGeoPoint.md)


### Example:

```php
$inputGeoPoint = ['_' => 'inputGeoPoint', 'latitude' => double, 'longitude' => double];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputGeoPoint", "latitude": double, "longitude": double}
```


Or, if you're into Lua:

```lua
inputGeoPoint={_='inputGeoPoint', latitude=double, longitude=double}

```


