---
title: upload.file
description: File content.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/upload_file.html
---
# Constructor: upload.file  
[Back to constructors index](index.md)



File content.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[storage.FileType](../constructors/storage.FileType.md) | Yes|File type|
|mtime|[int](../types/int.md) | Yes|Modification type|
|bytes|[bytes](../types/bytes.md) | Yes|Binary data, file content|



### Type: [upload.File](../types/upload.File.md)


### Example:

```php
$upload_file = ['_' => 'upload.file', 'type' => storage.FileType, 'mtime' => int, 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
upload_file={_='upload.file', type=storage.FileType, mtime=int, bytes='bytes'}

```


