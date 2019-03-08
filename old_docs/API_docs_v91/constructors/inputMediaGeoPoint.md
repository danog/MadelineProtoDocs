---
title: inputMediaGeoPoint
description: Media geo point
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaGeoPoint  
[Back to constructors index](index.md)



Media geo point

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geo point|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaGeoPoint = ['_' => 'inputMediaGeoPoint', 'geo_point' => InputGeoPoint];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaGeoPoint", "geo_point": InputGeoPoint}
```


Or, if you're into Lua:

```lua
inputMediaGeoPoint={_='inputMediaGeoPoint', geo_point=InputGeoPoint}

```


