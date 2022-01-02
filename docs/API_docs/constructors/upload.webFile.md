---
title: "upload.webFile"
description: "Represents a chunk of an HTTP webfile downloaded through telegram's secure MTProto servers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/upload_webFile.html
---
# Constructor: upload.webFile  
[Back to constructors index](index.md)



Represents a chunk of an [HTTP webfile](https://core.telegram.org/api/files) downloaded through telegram's secure MTProto servers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|size|[int](../types/int.md) | Yes|File size|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|file\_type|[storage.FileType](../constructors/storage.FileType.md) | Yes|File type|
|mtime|[int](../types/int.md) | Yes|Modified time|
|bytes|[bytes](../types/bytes.md) | Yes|Data|



### Type: [upload.WebFile](../types/upload.WebFile.md)


### Example:

```php
$upload_webFile = ['_' => 'upload.webFile', 'size' => int, 'mime_type' => 'string', 'file_type' => storage.FileType, 'mtime' => int, 'bytes' => 'bytes'];
```  


Or, if you're into Lua:

```lua
upload_webFile={_='upload.webFile', size=int, mime_type='string', file_type=storage.FileType, mtime=int, bytes='bytes'}

```


