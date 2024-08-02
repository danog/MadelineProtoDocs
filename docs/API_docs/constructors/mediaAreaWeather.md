---
title: "mediaAreaWeather"
description: "mediaAreaWeather attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaWeather  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|
|emoji|[string](/API_docs/types/string.html) | Yes|
|temperature\_c|[double](/API_docs/types/double.html) | Yes|
|color|[int](/API_docs/types/int.html) | Yes|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaWeather = ['_' => 'mediaAreaWeather', 'coordinates' => MediaAreaCoordinates, 'emoji' => 'string', 'temperature_c' => double, 'color' => int];
```  
