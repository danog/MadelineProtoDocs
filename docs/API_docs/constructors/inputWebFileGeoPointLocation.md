---
title: inputWebFileGeoPointLocation
description: inputWebFileGeoPointLocation attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebFileGeoPointLocation  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|
|access\_hash|[long](../types/long.md) | Yes|
|w|[int](../types/int.md) | Yes|
|h|[int](../types/int.md) | Yes|
|zoom|[int](../types/int.md) | Yes|
|scale|[int](../types/int.md) | Yes|



### Type: [InputWebFileLocation](../types/InputWebFileLocation.md)


### Example:

```
$inputWebFileGeoPointLocation = ['_' => 'inputWebFileGeoPointLocation', 'geo_point' => InputGeoPoint, 'access_hash' => long, 'w' => int, 'h' => int, 'zoom' => int, 'scale' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputWebFileGeoPointLocation", "geo_point": InputGeoPoint, "access_hash": long, "w": int, "h": int, "zoom": int, "scale": int}
```


Or, if you're into Lua:  


```
inputWebFileGeoPointLocation={_='inputWebFileGeoPointLocation', geo_point=InputGeoPoint, access_hash=long, w=int, h=int, zoom=int, scale=int}

```


