---
title: "upload.file"
description: "File content."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/upload_file.html
---
# Constructor: upload.file  
[Back to constructors index](/API_docs/constructors/index.html)



File content.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[storage.FileType](/API_docs/constructors/storage.FileType.html) | Yes|File type|
|mtime|[int](/API_docs/types/int.html) | Yes|Modification type|
|bytes|[bytes](/API_docs/types/bytes.html) | Yes|Binary data, file content|



### Type: [upload.File](/API_docs/types/upload.File.html)


### Example:

```
$upload_file = ['_' => 'upload.file', 'type' => storage.FileType, 'mtime' => int, 'bytes' => 'bytes'];
```  
