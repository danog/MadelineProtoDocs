---
title: inputMediaGeoLive
description: Media geo live
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaGeoLive  
[Back to constructors index](index.md)



Media geo live

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geo point|
|period|[int](../types/int.md) | Yes|Period|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaGeoLive = ['_' => 'inputMediaGeoLive', 'geo_point' => InputGeoPoint, 'period' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaGeoLive", "geo_point": InputGeoPoint, "period": int}
```


Or, if you're into Lua:

```lua
inputMediaGeoLive={_='inputMediaGeoLive', geo_point=InputGeoPoint, period=int}

```


