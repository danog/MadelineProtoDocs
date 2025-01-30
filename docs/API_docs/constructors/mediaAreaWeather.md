---
title: "mediaAreaWeather"
description: "Represents a weather widget »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaWeather  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [weather widget »](https://core.telegram.org/api/stories#weather).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|The size and location of the media area corresponding to the widget on top of the story media.|
|emoji|[string](/API_docs/types/string.html) | Yes|Weather emoji, should be rendered as an [animated emoji](https://core.telegram.org/api/animated-emojis).|
|temperature\_c|[double](/API_docs/types/double.html) | Yes|Temperature in degrees Celsius.|
|color|[int](/API_docs/types/int.html) | Yes|ARGB background color.|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaWeather = ['_' => 'mediaAreaWeather', 'coordinates' => MediaAreaCoordinates, 'emoji' => 'string', 'temperature_c' => double, 'color' => int];
```  
