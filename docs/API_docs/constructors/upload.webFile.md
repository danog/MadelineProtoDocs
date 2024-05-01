---
title: "upload.webFile"
description: "Represents a chunk of an HTTP webfile downloaded through telegram's secure MTProto servers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/upload_webFile.html
---
# Constructor: upload.webFile  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a chunk of an [HTTP webfile](https://core.telegram.org/api/files) downloaded through telegram's secure MTProto servers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|size|[int](/API_docs/types/int.html) | Yes|File size|
|mime\_type|[string](/API_docs/types/string.html) | Yes|Mime type|
|file\_type|[storage.FileType](/API_docs/constructors/storage.FileType.html) | Yes|File type|
|mtime|[int](/API_docs/types/int.html) | Yes|Modified time|
|bytes|[bytes](/API_docs/types/bytes.html) | Yes|Data|



### Type: [upload.WebFile](/API_docs/types/upload.WebFile.html)


### Example:

```
$upload_webFile = ['_' => 'upload.webFile', 'size' => int, 'mime_type' => 'string', 'file_type' => storage.FileType, 'mtime' => int, 'bytes' => 'bytes'];
```  
