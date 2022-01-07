---
title: "secureValueErrorFiles"
description: "Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorFiles  
[Back to constructors index](/API_docs/constructors/index.md)



Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.md) | Yes|One of [secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.md), [secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.md), [secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.md), [secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.md), [secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.md)|
|file\_hash|Array of [bytes](/API_docs/types/bytes.md) | Yes|File hash|
|text|[string](/API_docs/types/string.md) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.md)


### Example:

```php
$secureValueErrorFiles = ['_' => 'secureValueErrorFiles', 'type' => SecureValueType, 'file_hash' => ['bytes', 'bytes'], 'text' => 'string'];
```  
