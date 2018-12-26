---
title: decryptedMessageMediaVideo
description: Decrypted message media video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaVideo\_45  
[Back to constructors index](index.md)



Decrypted message media video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](../types/bytes.md) | Yes|Thumbnail|
|thumb\_w|[int](../types/int.md) | Yes|Thumbnail width|
|thumb\_h|[int](../types/int.md) | Yes|Thumbnail height|
|duration|[int](../types/int.md) | Yes|Duration|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|
|size|[int](../types/int.md) | Yes|Size|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaVideo_45 = ['_' => 'decryptedMessageMediaVideo', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'duration' => int, 'mime_type' => 'string', 'w' => int, 'h' => int, 'size' => int, 'caption' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaVideo", "thumb": {"_": "bytes", "bytes":"base64 encoded bytes"}, "thumb_w": int, "thumb_h": int, "duration": int, "mime_type": "string", "w": int, "h": int, "size": int, "caption": "string"}
```


Or, if you're into Lua:

```lua
decryptedMessageMediaVideo_45={_='decryptedMessageMediaVideo', thumb='bytes', thumb_w=int, thumb_h=int, duration=int, mime_type='string', w=int, h=int, size=int, caption='string'}

```


