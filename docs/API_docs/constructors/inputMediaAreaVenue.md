---
title: "inputMediaAreaVenue"
description: "Represents a location tag attached to a story, with additional venue information."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaAreaVenue  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [location tag](https://core.telegram.org/api/stories#media-areas) attached to a [story](https://core.telegram.org/api/stories), with additional venue information.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|The size and location of the media area corresponding to the location sticker on top of the story media.|
|query\_id|[long](/API_docs/types/long.html) | Yes|The `query_id` from [messages.botResults](../constructors/messages.botResults.html), see [here »](https://core.telegram.org/api/stories#media-areas) for more info.|
|result\_id|[string](/API_docs/types/string.html) | Yes|The `id` of the chosen result, see [here »](https://core.telegram.org/api/stories#media-areas) for more info.|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$inputMediaAreaVenue = ['_' => 'inputMediaAreaVenue', 'coordinates' => MediaAreaCoordinates, 'query_id' => long, 'result_id' => 'string'];
```  
