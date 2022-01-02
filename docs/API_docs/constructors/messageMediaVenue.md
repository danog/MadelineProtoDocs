---
title: "messageMediaVenue"
description: "Venue"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaVenue  
[Back to constructors index](index.md)



Venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geolocation of venue|
|title|[string](../types/string.md) | Yes|Venue name|
|address|[string](../types/string.md) | Yes|Address|
|provider|[string](../types/string.md) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](../types/string.md) | Yes|Venue ID in the provider's database|
|venue\_type|[string](../types/string.md) | Yes|Venue type in the provider's database|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaVenue = ['_' => 'messageMediaVenue', 'geo' => GeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string'];
```  


Or, if you're into Lua:

```lua
messageMediaVenue={_='messageMediaVenue', geo=GeoPoint, title='string', address='string', provider='string', venue_id='string', venue_type='string'}

```


