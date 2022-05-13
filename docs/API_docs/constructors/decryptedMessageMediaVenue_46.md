---
title: "decryptedMessageMediaVenue"
description: "Venue"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaVenue\_46  
[Back to constructors index](/API_docs/constructors/index.html)



Venue

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|lat|[double](/API_docs/types/double.html) | Yes|Latitude of venue|
|long|[double](/API_docs/types/double.html) | Yes|Longitude of venue|
|title|[string](/API_docs/types/string.html) | Yes|Venue name|
|address|[string](/API_docs/types/string.html) | Yes|Address|
|provider|[string](/API_docs/types/string.html) | Yes|Venue provider: currently only "foursquare" needs to be supported|
|venue\_id|[string](/API_docs/types/string.html) | Yes|Venue ID in the provider's database|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html)


### Example:

```
$decryptedMessageMediaVenue_46 = ['_' => 'decryptedMessageMediaVenue', 'lat' => double, 'long' => double, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string'];
```  
