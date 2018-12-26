---
title: messageMediaGeoLive
description: Message media geo live
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGeoLive  
[Back to constructors index](index.md)



Message media geo live

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geo|
|period|[int](../types/int.md) | Yes|Period|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaGeoLive = ['_' => 'messageMediaGeoLive', 'geo' => GeoPoint, 'period' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageMediaGeoLive", "geo": GeoPoint, "period": int}
```


Or, if you're into Lua:

```lua
messageMediaGeoLive={_='messageMediaGeoLive', geo=GeoPoint, period=int}

```


