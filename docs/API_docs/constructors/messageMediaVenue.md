---
title: "messageMediaVenue"
description: "Venue"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaVenue  
[Back to constructors index](/API_docs/constructors/index.html)



Venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|geo|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|Geolocation of venue|
|title|[string](/API_docs/types/string.html) | Yes|Venue name|
|address|[string](/API_docs/types/string.html) | Yes|Address|
|provider|[string](/API_docs/types/string.html) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](/API_docs/types/string.html) | Yes|Venue ID in the provider's database|
|venue\_type|[string](/API_docs/types/string.html) | Yes|Venue type in the provider's database|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaVenue = ['_' => 'messageMediaVenue', 'geo' => GeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string'];
```  
