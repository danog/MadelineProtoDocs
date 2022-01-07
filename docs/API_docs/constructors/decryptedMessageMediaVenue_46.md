---
title: "decryptedMessageMediaVenue"
description: "Venue"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaVenue\_46  
[Back to constructors index](/API_docs/constructors/index.md)



Venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lat|[double](/API_docs/types/double.md) | Yes|Latitude of venue|
|long|[double](/API_docs/types/double.md) | Yes|Longitude of venue|
|title|[string](/API_docs/types/string.md) | Yes|Venue name|
|address|[string](/API_docs/types/string.md) | Yes|Address|
|provider|[string](/API_docs/types/string.md) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](/API_docs/types/string.md) | Yes|Venue ID in the provider's database|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaVenue_46 = ['_' => 'decryptedMessageMediaVenue', 'lat' => double, 'long' => double, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string'];
```  
