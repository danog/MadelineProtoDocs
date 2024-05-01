---
title: "upload.cdnFile"
description: "Represent a chunk of a CDN file."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/upload_cdnFile.html
---
# Constructor: upload.cdnFile  
[Back to constructors index](/API_docs/constructors/index.html)



Represent a chunk of a [CDN](https://core.telegram.org/cdn) file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bytes|[bytes](/API_docs/types/bytes.html) | Yes|The data|



### Type: [upload.CdnFile](/API_docs/types/upload.CdnFile.html)


### Example:

```
$upload_cdnFile = ['_' => 'upload.cdnFile', 'bytes' => 'bytes'];
```  
