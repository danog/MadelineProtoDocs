---
title: "secureValueErrorFile"
description: "Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorFile  
[Back to constructors index](/API_docs/constructors/index.md)



Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.md) | Yes|One of [secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.md), [secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.md), [secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.md), [secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.md), [secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.md)|
|file\_hash|[bytes](/API_docs/types/bytes.md) | Yes|File hash|
|text|[string](/API_docs/types/string.md) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.md)


### Example:

```php
$secureValueErrorFile = ['_' => 'secureValueErrorFile', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  
