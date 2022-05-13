---
title: "wallPaperSettings"
description: "Wallpaper settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaperSettings  
[Back to constructors index](/API_docs/constructors/index.html)



Wallpaper settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blur|[Bool](/API_docs/types/Bool.html) | Optional|If set, the wallpaper must be downscaled to fit in 450x450 square and then box-blurred with radius 12|
|motion|[Bool](/API_docs/types/Bool.html) | Optional|If set, the background needs to be slightly moved when device is rotated|
|background\_color|[int](/API_docs/types/int.html) | Optional|If set, a PNG pattern is to be combined with the `color` chosen by the user: the main color of the background in RGB24 format|
|second\_background\_color|[int](/API_docs/types/int.html) | Optional|If set, a PNG pattern is to be combined with the first and second background colors (RGB24 format) in a top-bottom gradient|
|third\_background\_color|[int](/API_docs/types/int.html) | Optional|If set, a PNG pattern is to be combined with the first, second and third background colors (RGB24 format) in a freeform gradient|
|fourth\_background\_color|[int](/API_docs/types/int.html) | Optional|If set, a PNG pattern is to be combined with the first, second, third and fourth background colors (RGB24 format) in a freeform gradient|
|intensity|[int](/API_docs/types/int.html) | Optional|Intensity of the pattern when it is shown above the main background color, 0-100|
|rotation|[int](/API_docs/types/int.html) | Optional|Clockwise rotation angle of the gradient, in degrees; 0-359. Should be always divisible by 45|



### Type: [WallPaperSettings](/API_docs/types/WallPaperSettings.html)


### Example:

```
$wallPaperSettings = ['_' => 'wallPaperSettings', 'blur' => Bool, 'motion' => Bool, 'background_color' => int, 'second_background_color' => int, 'third_background_color' => int, 'fourth_background_color' => int, 'intensity' => int, 'rotation' => int];
```  
