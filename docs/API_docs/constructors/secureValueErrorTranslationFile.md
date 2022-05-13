---
title: "secureValueErrorTranslationFile"
description: "Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorTranslationFile  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.html) | Yes|One of [secureValueTypePersonalDetails](../constructors/secureValueTypePersonalDetails.html), [secureValueTypePassport](../constructors/secureValueTypePassport.html), [secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.html), [secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.html), [secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.html), [secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.html), [secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.html), [secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.html), [secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.html), [secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.html)|
|file\_hash|[bytes](/API_docs/types/bytes.html) | Yes|File hash|
|text|[string](/API_docs/types/string.html) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.html)


### Example:

```
$secureValueErrorTranslationFile = ['_' => 'secureValueErrorTranslationFile', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  
