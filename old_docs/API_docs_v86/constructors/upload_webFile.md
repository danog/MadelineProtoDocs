---
title: upload.webFile
description: Web file
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: upload.webFile  
[Back to constructors index](index.md)



Web file

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|size|[int](../types/int.md) | Yes|Size|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|file\_type|[storage\_FileType](../types/storage_FileType.md) | Yes|File type|
|mtime|[int](../types/int.md) | Yes|Mtime|
|bytes|[bytes](../types/bytes.md) | Yes|Bytes|



### Type: [upload\_WebFile](../types/upload_WebFile.md)


### Example:

```php
$upload_webFile = ['_' => 'upload.webFile', 'size' => int, 'mime_type' => 'string', 'file_type' => storage_FileType, 'mtime' => int, 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
upload_webFile={_='upload.webFile', size=int, mime_type='string', file_type=storage_FileType, mtime=int, bytes='bytes'}

```


