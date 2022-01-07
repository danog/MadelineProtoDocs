---
title: "secureData"
description: "Secure passport data, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureData  
[Back to constructors index](/API_docs/constructors/index.md)



Secure [passport](https://core.telegram.org/passport) data, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#securedata)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|data|[bytes](/API_docs/types/bytes.md) | Yes|Data|
|data\_hash|[bytes](/API_docs/types/bytes.md) | Yes|Data hash|
|secret|[bytes](/API_docs/types/bytes.md) | Yes|Secret|



### Type: [SecureData](/API_docs/types/SecureData.md)


### Example:

```php
$secureData = ['_' => 'secureData', 'data' => 'bytes', 'data_hash' => 'bytes', 'secret' => 'bytes'];
```  
