---
title: decryptedMessageMediaVideo
description: Decrypted message media video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaVideo\_8  
[Back to constructors index](index.md)



Decrypted message media video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](../types/bytes.md) | Yes|Thumbnail|
|thumb\_w|[int](../types/int.md) | Yes|Thumbnail width|
|thumb\_h|[int](../types/int.md) | Yes|Thumbnail height|
|duration|[int](../types/int.md) | Yes|Duration|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|
|size|[int](../types/int.md) | Yes|Size|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaVideo_8 = ['_' => 'decryptedMessageMediaVideo', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'duration' => int, 'w' => int, 'h' => int, 'size' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaVideo", "thumb": {"_": "bytes", "bytes":"base64 encoded bytes"}, "thumb_w": int, "thumb_h": int, "duration": int, "w": int, "h": int, "size": int}
```


Or, if you're into Lua:

```lua
decryptedMessageMediaVideo_8={_='decryptedMessageMediaVideo', thumb='bytes', thumb_w=int, thumb_h=int, duration=int, w=int, h=int, size=int}

```


