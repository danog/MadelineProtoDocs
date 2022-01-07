---
title: "secureValueErrorSelfie"
description: "Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorSelfie  
[Back to constructors index](/API_docs/constructors/index.md)



Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.md) | Yes|One of [secureValueTypePassport](../constructors/secureValueTypePassport.md), [secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.md), [secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.md), [secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.md)|
|file\_hash|[bytes](/API_docs/types/bytes.md) | Yes|File hash|
|text|[string](/API_docs/types/string.md) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.md)


### Example:

```php
$secureValueErrorSelfie = ['_' => 'secureValueErrorSelfie', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  
