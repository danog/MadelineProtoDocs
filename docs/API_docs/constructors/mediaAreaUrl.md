---
title: "mediaAreaUrl"
description: "Represents a URL media area."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaUrl  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [URL media area](https://core.telegram.org/api/stories#urls).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|The size and location of the media area corresponding to the URL button on top of the story media.|
|url|[string](/API_docs/types/string.html) | Yes|URL to open when clicked.|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaUrl = ['_' => 'mediaAreaUrl', 'coordinates' => MediaAreaCoordinates, 'url' => 'string'];
```  
