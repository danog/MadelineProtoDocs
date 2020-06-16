---
title: decryptedMessageMediaDocument
description: Document attached to a message in a secret chat.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaDocument\_8  
[Back to constructors index](index.md)



Document attached to a message in a secret chat.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|thumb|[bytes](../types/bytes.md) | Yes|Thumbnail-file contents (JPEG-file, quality 55, set in a 90x90 square)|
|thumb\_w|[int](../types/int.md) | Yes|Thumbnail width|
|thumb\_h|[int](../types/int.md) | Yes|Thumbnail height|
|file\_name|[string](../types/string.md) | Yes|
|mime\_type|[string](../types/string.md) | Yes|File MIME-type|
|size|[int](../types/int.md) | Yes|Document size|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaDocument_8 = ['_' => 'decryptedMessageMediaDocument', 'thumb' => 'bytes', 'thumb_w' => int, 'thumb_h' => int, 'file_name' => 'string', 'mime_type' => 'string', 'size' => int];
```  


Or, if you're into Lua:

```lua
decryptedMessageMediaDocument_8={_='decryptedMessageMediaDocument', thumb='bytes', thumb_w=int, thumb_h=int, file_name='string', mime_type='string', size=int}

```


