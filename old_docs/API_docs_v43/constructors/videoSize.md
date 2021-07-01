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
|location|[FileLocation](../types/FileLocation.md) | Yes|File location|
|w|[int](../types/int.md) | Yes|Video width|
|h|[int](../types/int.md) | Yes|Video height|
|size|[int](../types/int.md) | Yes|File size|



### Type: [VideoSize](../types/VideoSize.md)


### Example:

```php
$videoSize = ['_' => 'videoSize', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'size' => int];
```  


Or, if you're into Lua:

```lua
videoSize={_='videoSize', type='string', location=FileLocation, w=int, h=int, size=int}

```


