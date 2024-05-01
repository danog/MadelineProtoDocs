---
title: "mediaAreaVenue"
description: "Represents a location tag attached to a story, with additional venue information."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaVenue  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a location tag attached to a [story](https://core.telegram.org/api/stories), with additional venue information.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|The size and location of the media area corresponding to the location sticker on top of the story media.|
|geo|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|Coordinates of the venue|
|title|[string](/API_docs/types/string.html) | Yes|Venue name|
|address|[string](/API_docs/types/string.html) | Yes|Address|
|provider|[string](/API_docs/types/string.html) | Yes|Venue provider: currently only "foursquare" needs to be supported.|
|venue\_id|[string](/API_docs/types/string.html) | Yes|Venue ID in the provider's database|
|venue\_type|[string](/API_docs/types/string.html) | Yes|Venue type in the provider's database|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaVenue = ['_' => 'mediaAreaVenue', 'coordinates' => MediaAreaCoordinates, 'geo' => GeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string'];
```  
