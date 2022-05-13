---
title: "upload.fileCdnRedirect"
description: "The file must be downloaded from a CDN DC."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/upload_fileCdnRedirect.html
---
# Constructor: upload.fileCdnRedirect  
[Back to constructors index](/API_docs/constructors/index.html)



The file must be downloaded from a [CDN DC](https://core.telegram.org/cdn).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](/API_docs/types/int.html) | Yes|[CDN DC](https://core.telegram.org/cdn) ID|
|file\_token|[bytes](/API_docs/types/bytes.html) | Yes|File token (see [CDN files](https://core.telegram.org/cdn))|
|encryption\_key|[bytes](/API_docs/types/bytes.html) | Yes|Encryption key (see [CDN files](https://core.telegram.org/cdn))|
|encryption\_iv|[bytes](/API_docs/types/bytes.html) | Yes|Encryption IV (see [CDN files](https://core.telegram.org/cdn))|
|file\_hashes|Array of [FileHash](/API_docs/types/FileHash.html) | Yes|File hashes (see [CDN files](https://core.telegram.org/cdn))|



### Type: [upload.File](/API_docs/types/upload.File.html)


### Example:

```
$upload_fileCdnRedirect = ['_' => 'upload.fileCdnRedirect', 'dc_id' => int, 'file_token' => 'bytes', 'encryption_key' => 'bytes', 'encryption_iv' => 'bytes', 'file_hashes' => [FileHash, FileHash]];
```  
