---
title: "inputEncryptedFileLocation"
description: "Location of encrypted secret chat file."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFileLocation  
[Back to constructors index](/API_docs/constructors/index.md)



Location of encrypted secret chat file.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|File ID, **id** parameter value from [encryptedFile](../constructors/encryptedFile.md)|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Checksum, **access\_hash** parameter value from [encryptedFile](../constructors/encryptedFile.md)|



### Type: [InputFileLocation](/API_docs/types/InputFileLocation.md)


### Example:

```php
$inputEncryptedFileLocation = ['_' => 'inputEncryptedFileLocation', 'id' => long, 'access_hash' => long];
```  
