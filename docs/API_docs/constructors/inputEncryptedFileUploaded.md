---
title: "inputEncryptedFileUploaded"
description: "Sets new encrypted file saved by parts using upload.saveFilePart method."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFileUploaded  
[Back to constructors index](/API_docs/constructors/index.md)



Sets new encrypted file saved by parts using upload.saveFilePart method.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Random file ID created by clien|
|parts|[int](/API_docs/types/int.md) | Yes|Number of saved parts|
|md5\_checksum|[string](/API_docs/types/string.md) | Yes|In case [md5-HASH](https://en.wikipedia.org/wiki/MD5) of the (already encrypted) file was transmitted, file content will be checked prior to use|
|key\_fingerprint|[int](/API_docs/types/int.md) | Yes|32-bit fingerprint of the key used to encrypt a file|



### Type: [InputEncryptedFile](/API_docs/types/InputEncryptedFile.md)


### Example:

```php
$inputEncryptedFileUploaded = ['_' => 'inputEncryptedFileUploaded', 'id' => long, 'parts' => int, 'md5_checksum' => 'string', 'key_fingerprint' => int];
```  
