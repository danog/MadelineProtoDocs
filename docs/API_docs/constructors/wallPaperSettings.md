---
title: "wallPaperSettings"
description: "Wallpaper rendering information."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaperSettings  
[Back to constructors index](/API_docs/constructors/index.html)



[Wallpaper](https://core.telegram.org/api/wallpapers) rendering information.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|blur|[Bool](/API_docs/types/Bool.html) | Optional|For [image wallpapers »](https://core.telegram.org/api/wallpapers#image-wallpapers): if set, the JPEG must be downscaled to fit in 450x450 square and then box-blurred with radius 12.|
|motion|[Bool](/API_docs/types/Bool.html) | Optional|If set, the background needs to be slightly moved when the device is rotated.|
|background\_color|[int](/API_docs/types/int.html) | Optional|Used for [solid »](https://core.telegram.org/api/wallpapers#solid-fill), [gradient »](https://core.telegram.org/api/wallpapers#gradient-fill) and [freeform gradient »](https://core.telegram.org/api/wallpapers#freeform-gradient-fill) fills.|
|second\_background\_color|[int](/API_docs/types/int.html) | Optional|Used for [gradient »](https://core.telegram.org/api/wallpapers#gradient-fill) and [freeform gradient »](https://core.telegram.org/api/wallpapers#freeform-gradient-fill) fills.|
|third\_background\_color|[int](/API_docs/types/int.html) | Optional|Used for [freeform gradient »](https://core.telegram.org/api/wallpapers#freeform-gradient-fill) fills.|
|fourth\_background\_color|[int](/API_docs/types/int.html) | Optional|Used for [freeform gradient »](https://core.telegram.org/api/wallpapers#freeform-gradient-fill) fills.|
|intensity|[int](/API_docs/types/int.html) | Optional|Used for [pattern wallpapers »](https://core.telegram.org/api/wallpapers#pattern-wallpapers).|
|rotation|[int](/API_docs/types/int.html) | Optional|Clockwise rotation angle of the gradient, in degrees; 0-359. Should be always divisible by 45.|
|emoticon|[string](/API_docs/types/string.html) | Optional|If set, this wallpaper can be used as a channel wallpaper and is represented by the specified UTF-8 emoji.|



### Type: [WallPaperSettings](/API_docs/types/WallPaperSettings.html)


### Example:

```
$wallPaperSettings = ['_' => 'wallPaperSettings', 'blur' => Bool, 'motion' => Bool, 'background_color' => int, 'second_background_color' => int, 'third_background_color' => int, 'fourth_background_color' => int, 'intensity' => int, 'rotation' => int, 'emoticon' => 'string'];
```  
