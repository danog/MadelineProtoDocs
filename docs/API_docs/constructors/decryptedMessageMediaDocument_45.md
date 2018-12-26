---
title: decryptedMessageMediaDocument
description: Decrypted message media document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaDocument\_45  
[Back to constructors index](index.md)



Decrypted message media document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](../types/bytes.md) | Yes|Thumbnail|
|thumb\_w|[int](../types/int.md) | Yes|Thumbnail w|
|thumb\_h|[int](../types/int.md) | Yes|Thumbnail h|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|size|[int](../types/int.md) | Yes|Size|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaDocument_45 = ['_' => 'decryptedMessageMediaDocument', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'mime_type' => 'string', 'size' => int, 'attributes' => [DocumentAttribute, DocumentAttribute], 'caption' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "decryptedMessageMediaDocument", "thumb": {"_": "bytes", "bytes":"base64 encoded bytes"}, "thumb_w": int, "thumb_h": int, "mime_type": "string", "size": int, "attributes": [DocumentAttribute], "caption": "string"}
```


Or, if you're into Lua:

```lua
decryptedMessageMediaDocument_45={_='decryptedMessageMediaDocument', thumb='bytes', thumb_w=int, thumb_h=int, mime_type='string', size=int, attributes={DocumentAttribute}, caption='string'}

```


