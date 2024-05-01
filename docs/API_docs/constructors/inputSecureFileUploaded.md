---
title: "inputSecureFileUploaded"
description: "Uploaded secure file, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureFileUploaded  
[Back to constructors index](/API_docs/constructors/index.html)



Uploaded secure file, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#inputsecurefile)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Secure file ID|
|parts|[int](/API_docs/types/int.html) | Yes|Secure file part count|
|md5\_checksum|[string](/API_docs/types/string.html) | Yes|MD5 hash of encrypted uploaded file, to be checked server-side|
|file\_hash|[bytes](/API_docs/types/bytes.html) | Yes|File hash|
|secret|[bytes](/API_docs/types/bytes.html) | Yes|Secret|



### Type: [InputSecureFile](/API_docs/types/InputSecureFile.html)


### Example:

```
$inputSecureFileUploaded = ['_' => 'inputSecureFileUploaded', 'id' => long, 'parts' => int, 'md5_checksum' => 'string', 'file_hash' => 'bytes', 'secret' => 'bytes'];
```  
