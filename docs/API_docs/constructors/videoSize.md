---
title: "videoSize"
description: "Animated profile picture in MPEG4 format"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: videoSize  
[Back to constructors index](/API_docs/constructors/index.html)



[Animated profile picture](https://core.telegram.org/api/files#animated-profile-pictures) in MPEG4 format

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](/API_docs/types/string.html) | Yes|`u` for animated profile pictures, and `v` for trimmed and downscaled video previews|
|w|[int](/API_docs/types/int.html) | Yes|Video width|
|h|[int](/API_docs/types/int.html) | Yes|Video height|
|size|[int](/API_docs/types/int.html) | Yes|File size|
|video\_start\_ts|[double](/API_docs/types/double.html) | Optional|Timestamp that should be shown as static preview to the user (seconds)|



### Type: [VideoSize](/API_docs/types/VideoSize.html)


### Example:

```
$videoSize = ['_' => 'videoSize', 'type' => 'string', 'w' => int, 'h' => int, 'size' => int, 'video_start_ts' => double];
```  
