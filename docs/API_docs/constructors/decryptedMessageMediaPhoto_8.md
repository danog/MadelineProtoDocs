---
title: decryptedMessageMediaPhoto
description: Decrypted message media photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaPhoto\_8  
[Back to constructors index](index.md)



Decrypted message media photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](../types/bytes.md) | Yes|Thumbnail|
|thumb\_w|[int](../types/int.md) | Yes|Thumbnail width|
|thumb\_h|[int](../types/int.md) | Yes|Thumbnail height|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|
|size|[int](../types/int.md) | Yes|Size|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaPhoto_8 = ['_' => 'decryptedMessageMediaPhoto', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'w' => int, 'h' => int, 'size' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaPhoto", "thumb": {"_": "bytes", "bytes":"base64 encoded bytes"}, "thumb_w": int, "thumb_h": int, "w": int, "h": int, "size": int}
```


Or, if you're into Lua:

```lua
decryptedMessageMediaPhoto_8={_='decryptedMessageMediaPhoto', thumb='bytes', thumb_w=int, thumb_h=int, w=int, h=int, size=int}

```


