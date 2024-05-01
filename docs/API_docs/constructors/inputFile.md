---
title: "inputFile"
description: "Defines a file saved in parts using the method upload.saveFilePart."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputFile  
[Back to constructors index](/API_docs/constructors/index.html)



Defines a file saved in parts using the method [upload.saveFilePart](../methods/upload.saveFilePart.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Random file identifier created by the client|
|parts|[int](/API_docs/types/int.html) | Yes|Number of parts saved|
|name|[string](/API_docs/types/string.html) | Yes|Full name of the file|
|md5\_checksum|[string](/API_docs/types/string.html) | Yes|In case the file's [md5-hash](https://en.wikipedia.org/wiki/MD5#MD5_hashes) was passed, contents of the file will be checked prior to use|



### Type: [InputFile](/API_docs/types/InputFile.html)


### Example:

```
$inputFile = ['_' => 'inputFile', 'id' => long, 'parts' => int, 'name' => 'string', 'md5_checksum' => 'string'];
```  
