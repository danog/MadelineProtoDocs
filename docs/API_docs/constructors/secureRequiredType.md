---
title: "secureRequiredType"
description: "Required type"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureRequiredType  
[Back to constructors index](/API_docs/constructors/index.md)



Required type

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|native\_names|[Bool](/API_docs/types/Bool.md) | Optional|Native names|
|selfie\_required|[Bool](/API_docs/types/Bool.md) | Optional|Is a selfie required|
|translation\_required|[Bool](/API_docs/types/Bool.md) | Optional|Is a translation required|
|type|[SecureValueType](/API_docs/types/SecureValueType.md) | Yes|Secure value type|



### Type: [SecureRequiredType](/API_docs/types/SecureRequiredType.md)


### Example:

```php
$secureRequiredType = ['_' => 'secureRequiredType', 'native_names' => Bool, 'selfie_required' => Bool, 'translation_required' => Bool, 'type' => SecureValueType];
```  
