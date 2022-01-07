---
title: "inputEncryptedFile"
description: "Sets forwarded encrypted file for attachment."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputEncryptedFile  
[Back to constructors index](index.md)



Sets forwarded encrypted file for attachment.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|File ID, value of **id** parameter from [encryptedFile](../constructors/encryptedFile.md)|
|access\_hash|[long](../types/long.md) | Yes|Checking sum, value of **access\_hash** parameter from [encryptedFile](../constructors/encryptedFile.md)|



### Type: [InputEncryptedFile](../types/InputEncryptedFile.md)


### Example:

```php
$inputEncryptedFile = ['_' => 'inputEncryptedFile', 'id' => long, 'access_hash' => long];
```  
