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
|stopped|[Bool](../types/Bool.md) | Optional|Stopped?|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geo point|
|period|[int](../types/int.md) | Optional|Period|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaGeoLive = ['_' => 'inputMediaGeoLive', 'stopped' => Bool, 'geo_point' => InputGeoPoint, 'period' => int];
```  


Or, if you're into Lua:

```lua
inputMediaGeoLive={_='inputMediaGeoLive', stopped=Bool, geo_point=InputGeoPoint, period=int}

```


