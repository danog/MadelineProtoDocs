---
title: inputMediaVenue
description: Media venue
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaVenue  
[Back to constructors index](index.md)



Media venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geo point|
|title|[string](../types/string.md) | Yes|Title|
|address|[string](../types/string.md) | Yes|Address|
|provider|[string](../types/string.md) | Yes|Provider|
|venue\_id|[string](../types/string.md) | Yes|Venue ID|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaVenue = ['_' => 'inputMediaVenue', 'geo_point' => InputGeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaVenue", "geo_point": InputGeoPoint, "title": "string", "address": "string", "provider": "string", "venue_id": "string"}
```


Or, if you're into Lua:

```lua
inputMediaVenue={_='inputMediaVenue', geo_point=InputGeoPoint, title='string', address='string', provider='string', venue_id='string'}

```


