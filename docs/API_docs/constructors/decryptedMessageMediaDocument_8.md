---
title: decryptedMessageMediaDocument
description: Decrypted message media document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaDocument\_8  
[Back to constructors index](index.md)



Decrypted message media document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](../types/bytes.md) | Yes|Thumbnail|
|thumb\_w|[int](../types/int.md) | Yes|Thumbnail w|
|thumb\_h|[int](../types/int.md) | Yes|Thumbnail h|
|file\_name|[string](../types/string.md) | Yes|File name|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|size|[int](../types/int.md) | Yes|Size|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaDocument_8 = ['_' => 'decryptedMessageMediaDocument', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'file_name' => 'string', 'mime_type' => 'string', 'size' => int];
```  


Or, if you're into Lua:

```lua
decryptedMessageMediaDocument_8={_='decryptedMessageMediaDocument', thumb='bytes', thumb_w=int, thumb_h=int, file_name='string', mime_type='string', size=int}

```


