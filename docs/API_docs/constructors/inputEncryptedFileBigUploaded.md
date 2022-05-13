---
title: "inputEncryptedFileBigUploaded"
description: "Assigns a new big encrypted file (over 10 MB in size), saved in parts using the method upload.saveBigFilePart."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFileBigUploaded  
[Back to constructors index](/API_docs/constructors/index.html)



Assigns a new big encrypted file (over 10 MB in size), saved in parts using the method [upload.saveBigFilePart](../methods/upload.saveBigFilePart.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Random file id, created by the client|
|parts|[int](/API_docs/types/int.html) | Yes|Number of saved parts|
|key\_fingerprint|[int](/API_docs/types/int.html) | Yes|32-bit imprint of the key used to encrypt the file|



### Type: [InputEncryptedFile](/API_docs/types/InputEncryptedFile.html)


### Example:

```
$inputEncryptedFileBigUploaded = ['_' => 'inputEncryptedFileBigUploaded', 'id' => long, 'parts' => int, 'key_fingerprint' => int];
```  
