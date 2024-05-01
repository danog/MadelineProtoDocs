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
|file\_token|[string](/API_docs/types/string.html) | Yes|
|encryption\_key|[string](/API_docs/types/string.html) | Yes|
|encryption\_iv|[string](/API_docs/types/string.html) | Yes|
|file\_hashes|Array of [FileHash](/API_docs/types/FileHash.html) | Yes|File hashes (see [CDN files](https://core.telegram.org/cdn))|



### Type: [upload.File](/API_docs/types/upload.File.html)


### Example:

```
$upload_fileCdnRedirect = ['_' => 'upload.fileCdnRedirect', 'dc_id' => int, 'file_token' => 'string', 'encryption_key' => 'string', 'encryption_iv' => 'string', 'file_hashes' => [FileHash, FileHash]];
```  
