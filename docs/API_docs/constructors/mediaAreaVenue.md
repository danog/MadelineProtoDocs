---
title: "mediaAreaVenue"
description: "mediaAreaVenue attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaVenue  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|
|geo|[GeoPoint](/API_docs/types/GeoPoint.html) | Optional|
|title|[string](/API_docs/types/string.html) | Yes|
|address|[string](/API_docs/types/string.html) | Yes|
|provider|[string](/API_docs/types/string.html) | Yes|
|venue\_id|[string](/API_docs/types/string.html) | Yes|
|venue\_type|[string](/API_docs/types/string.html) | Yes|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaVenue = ['_' => 'mediaAreaVenue', 'coordinates' => MediaAreaCoordinates, 'geo' => GeoPoint, 'title' => 'string', 'address' => 'string', 'provider' => 'string', 'venue_id' => 'string', 'venue_type' => 'string'];
```  
