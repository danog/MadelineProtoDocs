---
title: "inputEncryptedFile"
description: "Sets forwarded encrypted file for attachment."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFile  
[Back to constructors index](/API_docs/constructors/index.html)



Sets forwarded encrypted file for attachment.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|File ID, value of **id** parameter from [encryptedFile](../constructors/encryptedFile.html)|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Checking sum, value of **access\_hash** parameter from [encryptedFile](../constructors/encryptedFile.html)|



### Type: [InputEncryptedFile](/API_docs/types/InputEncryptedFile.html)


### Example:

```
$inputEncryptedFile = ['_' => 'inputEncryptedFile', 'id' => long, 'access_hash' => long];
```  
