---
title: "secureValueErrorFrontSide"
description: "Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorFrontSide  
[Back to constructors index](index.md)



Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|One of [secureValueTypePassport](../constructors/secureValueTypePassport.md), [secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.md), [secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.md), [secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.md)|
|file\_hash|[bytes](../types/bytes.md) | Yes|File hash|
|text|[string](../types/string.md) | Yes|Error message|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueErrorFrontSide = ['_' => 'secureValueErrorFrontSide', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  
