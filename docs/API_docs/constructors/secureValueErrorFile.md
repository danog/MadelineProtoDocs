---
title: "secureValueErrorFile"
description: "Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorFile  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.html) | Yes|One of [secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.html), [secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.html), [secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.html), [secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.html), [secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.html)|
|file\_hash|[bytes](/API_docs/types/bytes.html) | Yes|File hash|
|text|[string](/API_docs/types/string.html) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.html)


### Example:

```
$secureValueErrorFile = ['_' => 'secureValueErrorFile', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  
