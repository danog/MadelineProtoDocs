---
title: "encryptedFile"
description: "Encrypted file."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedFile  
[Back to constructors index](/API_docs/constructors/index.html)



Encrypted file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|File ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Checking sum depending on user ID|
|size|[int](/API_docs/types/int.html) | Yes|File size in bytes|
|dc\_id|[int](/API_docs/types/int.html) | Yes|Number of data center|
|key\_fingerprint|[int](/API_docs/types/int.html) | Yes|32-bit fingerprint of key used for file encryption|



### Type: [EncryptedFile](/API_docs/types/EncryptedFile.html)


### Example:

```php
$encryptedFile = ['_' => 'encryptedFile', 'id' => long, 'access_hash' => long, 'size' => int, 'dc_id' => int, 'key_fingerprint' => int];
```  
