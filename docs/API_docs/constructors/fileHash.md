---
title: "fileHash"
description: "SHA256 Hash of an uploaded file, to be checked for validity after download"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: fileHash  
[Back to constructors index](/API_docs/constructors/index.html)



SHA256 Hash of an uploaded file, to be checked for validity after download

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[long](/API_docs/types/long.html) | Yes|
|limit|[int](/API_docs/types/int.html) | Yes|Length|
|hash|[bytes](/API_docs/types/bytes.html) | Yes|SHA-256 Hash of file chunk, to be checked for validity after download|



### Type: [FileHash](/API_docs/types/FileHash.html)


### Example:

```
$fileHash = ['_' => 'fileHash', 'offset' => long, 'limit' => int, 'hash' => 'bytes'];
```  
