---
title: "inputMediaVenue"
description: "Can be used to send a venue geolocation."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaVenue  
[Back to constructors index](index.md)



Can be used to send a venue geolocation.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](../types/InputGeoPoint.md) | Optional|Geolocation|
|title|[string](../types/string.md) | Yes|Venue name|
|address|[string](../types/string.md) | Yes|Physical address of the venue|
|provider|[string](../types/string.md) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](../types/string.md) | Yes|Venue ID in the provider's database|
|venue\_type|[string](../types/string.md) | Yes|Venue type in the provider's database|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaVenue = ['_' => 'inputMediaVenue', 'geo_point' => InputGeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaVenue={_='inputMediaVenue', geo_point=InputGeoPoint, title='string', address='string', provider='string', venue_id='string', venue_type='string'}

```


