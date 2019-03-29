---
title: inputWebFileGeoPointLocation
description: Web file geo point location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebFileGeoPointLocation  
[Back to constructors index](index.md)



Web file geo point location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geo point|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|
|zoom|[int](../types/int.md) | Yes|Zoom|
|scale|[int](../types/int.md) | Yes|Scale|



### Type: [InputWebFileLocation](../types/InputWebFileLocation.md)


### Example:

```php
$inputWebFileGeoPointLocation = ['_' => 'inputWebFileGeoPointLocation', 'geo_point' => InputGeoPoint, 'access_hash' => long, 'w' => int, 'h' => int, 'zoom' => int, 'scale' => int];
```  


Or, if you're into Lua:

```lua
inputWebFileGeoPointLocation={_='inputWebFileGeoPointLocation', geo_point=InputGeoPoint, access_hash=long, w=int, h=int, zoom=int, scale=int}

```


