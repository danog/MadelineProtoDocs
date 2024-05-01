---
title: "inputFileBig"
description: "Assigns a big file (over 10 MB in size), saved in part using the method upload.saveBigFilePart."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFileBig  
[Back to constructors index](/API_docs/constructors/index.html)



Assigns a big file (over 10 MB in size), saved in part using the method [upload.saveBigFilePart](../methods/upload.saveBigFilePart.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Random file id, created by the client|
|parts|[int](/API_docs/types/int.html) | Yes|Number of parts saved|
|name|[string](/API_docs/types/string.html) | Yes|Full file name|



### Type: [InputFile](/API_docs/types/InputFile.html)


### Example:

```
$inputFileBig = ['_' => 'inputFileBig', 'id' => long, 'parts' => int, 'name' => 'string'];
```  
