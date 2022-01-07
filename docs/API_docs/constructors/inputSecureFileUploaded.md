---
title: "inputSecureFileUploaded"
description: "Uploaded secure file, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFileUploaded  
[Back to constructors index](/API_docs/constructors/index.md)



Uploaded secure file, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#inputsecurefile)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Secure file ID|
|parts|[int](/API_docs/types/int.md) | Yes|Secure file part count|
|md5\_checksum|[string](/API_docs/types/string.md) | Yes|MD5 hash of encrypted uploaded file, to be checked server-side|
|file\_hash|[bytes](/API_docs/types/bytes.md) | Yes|File hash|
|secret|[bytes](/API_docs/types/bytes.md) | Yes|Secret|



### Type: [InputSecureFile](/API_docs/types/InputSecureFile.md)


### Example:

```php
$inputSecureFileUploaded = ['_' => 'inputSecureFileUploaded', 'id' => long, 'parts' => int, 'md5_checksum' => 'string', 'file_hash' => 'bytes', 'secret' => 'bytes'];
```  
