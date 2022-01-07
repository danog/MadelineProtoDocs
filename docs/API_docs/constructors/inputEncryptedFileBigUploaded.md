---
title: "inputEncryptedFileBigUploaded"
description: "Assigns a new big encrypted file (over 10Mb in size), saved in parts using the method upload.saveBigFilePart."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFileBigUploaded  
[Back to constructors index](index.md)



Assigns a new big encrypted file (over 10Mb in size), saved in parts using the method [upload.saveBigFilePart](../methods/upload.saveBigFilePart.md).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Random file id, created by the client|
|parts|[int](../types/int.md) | Yes|Number of saved parts|
|key\_fingerprint|[int](../types/int.md) | Yes|32-bit imprint of the key used to encrypt the file|



### Type: [InputEncryptedFile](../types/InputEncryptedFile.md)


### Example:

```php
$inputEncryptedFileBigUploaded = ['_' => 'inputEncryptedFileBigUploaded', 'id' => long, 'parts' => int, 'key_fingerprint' => int];
```  
