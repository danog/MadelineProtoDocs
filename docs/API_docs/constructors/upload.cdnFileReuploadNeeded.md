---
title: "upload.cdnFileReuploadNeeded"
description: "The file was cleared from the temporary RAM cache of the CDN and has to be re-uploaded."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/upload_cdnFileReuploadNeeded.html
---
# Constructor: upload.cdnFileReuploadNeeded  
[Back to constructors index](/API_docs/constructors/index.html)



The file was cleared from the temporary RAM cache of the [CDN](https://core.telegram.org/cdn) and has to be re-uploaded.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|request\_token|[bytes](/API_docs/types/bytes.html) | Yes|Request token (see [CDN](https://core.telegram.org/cdn))|



### Type: [upload.CdnFile](/API_docs/types/upload.CdnFile.html)


### Example:

```
$upload_cdnFileReuploadNeeded = ['_' => 'upload.cdnFileReuploadNeeded', 'request_token' => 'bytes'];
```  
