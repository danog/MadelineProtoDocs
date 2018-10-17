---
title: decryptedMessageMediaVideo
description: decryptedMessageMediaVideo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaVideo\_17  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|thumb|[bytes](../types/bytes.md) | Yes|
|thumb\_w|[int](../types/int.md) | Yes|
|thumb\_h|[int](../types/int.md) | Yes|
|duration|[int](../types/int.md) | Yes|
|mime\_type|[string](../types/string.md) | Yes|
|w|[int](../types/int.md) | Yes|
|h|[int](../types/int.md) | Yes|
|size|[int](../types/int.md) | Yes|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaVideo_17 = ['_' => 'decryptedMessageMediaVideo', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'duration' => int, 'mime_type' => 'string', 'w' => int, 'h' => int, 'size' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaVideo", "thumb": {"_": "bytes", "bytes":"base64 encoded bytes"}, "thumb_w": int, "thumb_h": int, "duration": int, "mime_type": "string", "w": int, "h": int, "size": int}
```


Or, if you're into Lua:

```lua
decryptedMessageMediaVideo_17={_='decryptedMessageMediaVideo', thumb='bytes', thumb_w=int, thumb_h=int, duration=int, mime_type='string', w=int, h=int, size=int}

```


