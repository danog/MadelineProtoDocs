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
|lat|[double](../types/double.md) | Yes|Lat|
|long|[double](../types/double.md) | Yes|Long|



### Type: [InputGeoPoint](../types/InputGeoPoint.md)


### Example:

```php
$inputGeoPoint = ['_' => 'inputGeoPoint', 'lat' => double, 'long' => double];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputGeoPoint", "lat": double, "long": double}
```


Or, if you're into Lua:

```lua
inputGeoPoint={_='inputGeoPoint', lat=double, long=double}

```


