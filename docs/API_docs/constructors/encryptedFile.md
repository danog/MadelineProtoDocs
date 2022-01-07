---
title: "encryptedFile"
description: "Encrypted file."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedFile  
[Back to constructors index](/API_docs/constructors/index.md)



Encrypted file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|File ID|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Checking sum depending on user ID|
|size|[int](/API_docs/types/int.md) | Yes|File size in bytes|
|dc\_id|[int](/API_docs/types/int.md) | Yes|Number of data centre|
|key\_fingerprint|[int](/API_docs/types/int.md) | Yes|32-bit fingerprint of key used for file encryption|



### Type: [EncryptedFile](/API_docs/types/EncryptedFile.md)


### Example:

```php
$encryptedFile = ['_' => 'encryptedFile', 'id' => long, 'access_hash' => long, 'size' => int, 'dc_id' => int, 'key_fingerprint' => int];
```  
