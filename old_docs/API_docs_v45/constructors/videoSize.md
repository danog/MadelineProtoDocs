---
title: videoSize
description: videoSize attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: videoSize  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[string](../types/string.md) | Yes|
|location|[FileLocation](../types/FileLocation.md) | Yes|
|w|[int](../types/int.md) | Yes|
|h|[int](../types/int.md) | Yes|
|size|[int](../types/int.md) | Yes|
|video\_start\_ts|[double](../types/double.md) | Optional|



### Type: [VideoSize](../types/VideoSize.md)


### Example:

```php
$videoSize = ['_' => 'videoSize', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'size' => int, 'video_start_ts' => double];
```  


Or, if you're into Lua:

```lua
videoSize={_='videoSize', type='string', location=FileLocation, w=int, h=int, size=int, video_start_ts=double}

```


