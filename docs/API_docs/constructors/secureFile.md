---
title: "secureFile"
description: "Secure passport file, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureFile  
[Back to constructors index](/API_docs/constructors/index.html)



Secure [passport](https://core.telegram.org/passport) file, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#inputsecurefile)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|size|[long](/API_docs/types/long.html) | Yes|
|dc\_id|[int](/API_docs/types/int.html) | Yes|DC ID|
|date|[int](/API_docs/types/int.html) | Yes|Date of upload|
|file\_hash|[bytes](/API_docs/types/bytes.html) | Yes|File hash|
|secret|[bytes](/API_docs/types/bytes.html) | Yes|Secret|



### Type: [SecureFile](/API_docs/types/SecureFile.html)


### Example:

```
$secureFile = ['_' => 'secureFile', 'id' => long, 'access_hash' => long, 'size' => long, 'dc_id' => int, 'date' => int, 'file_hash' => 'bytes', 'secret' => 'bytes'];
```  
