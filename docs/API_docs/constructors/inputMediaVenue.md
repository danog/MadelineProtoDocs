---
title: "inputMediaVenue"
description: "Can be used to send a venue geolocation."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaVenue  
[Back to constructors index](/API_docs/constructors/index.md)



Can be used to send a venue geolocation.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo\_point|[InputGeoPoint](/API_docs/types/InputGeoPoint.md) | Optional|Geolocation|
|title|[string](/API_docs/types/string.md) | Yes|Venue name|
|address|[string](/API_docs/types/string.md) | Yes|Physical address of the venue|
|provider|[string](/API_docs/types/string.md) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](/API_docs/types/string.md) | Yes|Venue ID in the provider's database|
|venue\_type|[string](/API_docs/types/string.md) | Yes|Venue type in the provider's database|



### Type: [InputMedia](/API_docs/types/InputMedia.md)


### Example:

```php
$inputMediaVenue = ['_' => 'inputMediaVenue', 'geo_point' => InputGeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string'];
```  
