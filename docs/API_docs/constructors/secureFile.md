---
title: "secureFile"
description: "Secure passport file, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureFile  
[Back to constructors index](index.md)



Secure [passport](https://core.telegram.org/passport) file, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#inputsecurefile)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|size|[int](../types/int.md) | Yes|File size|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|date|[int](../types/int.md) | Yes|Date of upload|
|file\_hash|[bytes](../types/bytes.md) | Yes|File hash|
|secret|[bytes](../types/bytes.md) | Yes|Secret|



### Type: [SecureFile](../types/SecureFile.md)


### Example:

```php
$secureFile = ['_' => 'secureFile', 'id' => long, 'access_hash' => long, 'size' => int, 'dc_id' => int, 'date' => int, 'file_hash' => 'bytes', 'secret' => 'bytes'];
```  
