---
title: "decryptedMessageMediaVideo"
description: "Video attached to an encrypted message."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaVideo\_8  
[Back to constructors index](index.md)



Video attached to an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](../types/bytes.md) | Yes|Content of thumbnail file (JPEG file, quality 55, set in a square 90x90)|
|thumb\_w|[int](../types/int.md) | Yes|Thumbnail width|
|thumb\_h|[int](../types/int.md) | Yes|Thumbnail height|
|duration|[int](../types/int.md) | Yes|Duration of video in seconds|
|w|[int](../types/int.md) | Yes|Image width|
|h|[int](../types/int.md) | Yes|Image height|
|size|[int](../types/int.md) | Yes|File size|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaVideo_8 = ['_' => 'decryptedMessageMediaVideo', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'duration' => int, 'w' => int, 'h' => int, 'size' => int];
```  


Or, if you're into Lua:

```lua
decryptedMessageMediaVideo_8={_='decryptedMessageMediaVideo', thumb='bytes', thumb_w=int, thumb_h=int, duration=int, w=int, h=int, size=int}

```


