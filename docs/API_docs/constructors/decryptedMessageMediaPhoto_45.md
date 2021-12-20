---
title: "decryptedMessageMediaPhoto"
description: "Photo attached to an encrypted message."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaPhoto\_45  
[Back to constructors index](index.md)



Photo attached to an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](../types/bytes.md) | Yes|Content of thumbnail file (JPEGfile, quality 55, set in a square 90x90)|
|thumb\_w|[int](../types/int.md) | Yes|Thumbnail width|
|thumb\_h|[int](../types/int.md) | Yes|Thumbnail height|
|w|[int](../types/int.md) | Yes|Photo width|
|h|[int](../types/int.md) | Yes|Photo height|
|size|[int](../types/int.md) | Yes|Size of the photo in bytes|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaPhoto_45 = ['_' => 'decryptedMessageMediaPhoto', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'w' => int, 'h' => int, 'size' => int, 'caption' => 'string'];
```  


Or, if you're into Lua:

```lua
decryptedMessageMediaPhoto_45={_='decryptedMessageMediaPhoto', thumb='bytes', thumb_w=int, thumb_h=int, w=int, h=int, size=int, caption='string'}

```


