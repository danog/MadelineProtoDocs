---
title: decryptedMessageMediaPhoto
description: decryptedMessageMediaPhoto attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaPhoto\_8  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|thumb|[bytes](../types/bytes.md) | Yes|
|thumb\_w|[int](../types/int.md) | Yes|
|thumb\_h|[int](../types/int.md) | Yes|
|w|[int](../types/int.md) | Yes|
|h|[int](../types/int.md) | Yes|
|size|[int](../types/int.md) | Yes|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```
$decryptedMessageMediaPhoto_8 = ['_' => 'decryptedMessageMediaPhoto', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'w' => int, 'h' => int, 'size' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaPhoto", "thumb": {"_": "bytes", "bytes":"base64 encoded bytes"}, "thumb_w": int, "thumb_h": int, "w": int, "h": int, "size": int}
```


Or, if you're into Lua:  


```
decryptedMessageMediaPhoto_8={_='decryptedMessageMediaPhoto', thumb='bytes', thumb_w=int, thumb_h=int, w=int, h=int, size=int}

```


