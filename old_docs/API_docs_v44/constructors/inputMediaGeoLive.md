---
title: inputMediaGeoLive
description: Live geographical location
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaGeoLive  
[Back to constructors index](index.md)



Live geographical location

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stopped|[Bool](../types/Bool.md) | Optional|Whether sending of the geolocation was stopped|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Current geolocation|
|period|[int](../types/int.md) | Optional|Validity period of the current location|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaGeoLive = ['_' => 'inputMediaGeoLive', 'stopped' => Bool, 'geo_point' => InputGeoPoint, 'period' => int];
```  


Or, if you're into Lua:

```lua
inputMediaGeoLive={_='inputMediaGeoLive', stopped=Bool, geo_point=InputGeoPoint, period=int}

```


