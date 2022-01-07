---
title: "secureSecretSettings"
description: "Secure settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureSecretSettings  
[Back to constructors index](/API_docs/constructors/index.md)



Secure settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|secure\_algo|[SecurePasswordKdfAlgo](/API_docs/types/SecurePasswordKdfAlgo.md) | Yes|Secure KDF algo|
|secure\_secret|[bytes](/API_docs/types/bytes.md) | Yes|Secure secret|
|secure\_secret\_id|[long](/API_docs/types/long.md) | Yes|Secret ID|



### Type: [SecureSecretSettings](/API_docs/types/SecureSecretSettings.md)


### Example:

```php
$secureSecretSettings = ['_' => 'secureSecretSettings', 'secure_algo' => SecurePasswordKdfAlgo, 'secure_secret' => 'bytes', 'secure_secret_id' => long];
```  
