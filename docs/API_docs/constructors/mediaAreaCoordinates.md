---
title: "mediaAreaCoordinates"
description: "Coordinates and size of a clickable rectangular area on top of a story."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaCoordinates  
[Back to constructors index](/API_docs/constructors/index.html)



Coordinates and size of a clickable rectangular area on top of a story.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|x|[double](/API_docs/types/double.html) | Yes|The abscissa of the rectangle's center, as a percentage of the media width (0-100).|
|y|[double](/API_docs/types/double.html) | Yes|The ordinate of the rectangle's center, as a percentage of the media height (0-100).|
|w|[double](/API_docs/types/double.html) | Yes|The width of the rectangle, as a percentage of the media width (0-100).|
|h|[double](/API_docs/types/double.html) | Yes|The height of the rectangle, as a percentage of the media height (0-100).|
|rotation|[double](/API_docs/types/double.html) | Yes|Clockwise rotation angle of the rectangle, in degrees (0-360).|
|radius|[double](/API_docs/types/double.html) | Optional|The radius of the rectangle corner rounding, as a percentage of the media width.|



### Type: [MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html)


### Example:

```
$mediaAreaCoordinates = ['_' => 'mediaAreaCoordinates', 'x' => double, 'y' => double, 'w' => double, 'h' => double, 'rotation' => double, 'radius' => double];
```  
