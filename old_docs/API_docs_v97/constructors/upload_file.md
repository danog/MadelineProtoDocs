---
title: upload.file
description: File
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: upload.file  
[Back to constructors index](index.md)



File

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[storage\_FileType](../types/storage_FileType.md) | Yes|Type|
|mtime|[int](../types/int.md) | Yes|Mtime|
|bytes|[bytes](../types/bytes.md) | Yes|Bytes|



### Type: [upload\_File](../types/upload_File.md)


### Example:

```php
$upload_file = ['_' => 'upload.file', 'type' => storage_FileType, 'mtime' => int, 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
upload_file={_='upload.file', type=storage_FileType, mtime=int, bytes='bytes'}

```


