---
title: videoSize
description: [Animated profile picture](https://core.telegram.org/api/files#animated-profile-pictures) in MPEG4 format
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: videoSize  
[Back to constructors index](index.md)



[Animated profile picture](https://core.telegram.org/api/files#animated-profile-pictures) in MPEG4 format

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|`u` for animated profile pictures, and `v` for trimmed and downscaled video previews|
|w|[int](../types/int.md) | Yes|Video width|
|h|[int](../types/int.md) | Yes|Video height|
|size|[int](../types/int.md) | Yes|File size|
|video\_start\_ts|[double](../types/double.md) | Optional|Timestamp that should be shown as static preview to the user (seconds)|



### Type: [VideoSize](../types/VideoSize.md)


### Example:

```php
$videoSize = ['_' => 'videoSize', 'type' => 'string', 'w' => int, 'h' => int, 'size' => int, 'video_start_ts' => double];
```  


Or, if you're into Lua:

```lua
videoSize={_='videoSize', type='string', w=int, h=int, size=int, video_start_ts=double}

```


