---
title: "secureValueErrorFiles"
description: "Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorFiles  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.html) | Yes|One of [secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.html), [secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.html), [secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.html), [secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.html), [secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.html)|
|file\_hash|Array of [bytes](/API_docs/types/bytes.html) | Yes|File hash|
|text|[string](/API_docs/types/string.html) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.html)


### Example:

```
$secureValueErrorFiles = ['_' => 'secureValueErrorFiles', 'type' => SecureValueType, 'file_hash' => ['bytes', 'bytes'], 'text' => 'string'];
```  
