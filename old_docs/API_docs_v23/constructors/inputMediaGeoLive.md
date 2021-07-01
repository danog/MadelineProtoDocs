---
title: inputMediaGeoLive
description: [Live geolocation](https://core.telegram.org/api/live-location)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaGeoLive  
[Back to constructors index](index.md)



[Live geolocation](https://core.telegram.org/api/live-location)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Current geolocation|
|period|[int](../types/int.md) | Yes|Validity period of the current location|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaGeoLive = ['_' => 'inputMediaGeoLive', 'geo_point' => InputGeoPoint, 'period' => int];
```  


Or, if you're into Lua:

```lua
inputMediaGeoLive={_='inputMediaGeoLive', geo_point=InputGeoPoint, period=int}

```


