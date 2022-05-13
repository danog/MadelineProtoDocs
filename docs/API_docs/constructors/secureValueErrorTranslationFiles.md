---
title: "secureValueErrorTranslationFiles"
description: "Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorTranslationFiles  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.html) | Yes|One of [secureValueTypePersonalDetails](../constructors/secureValueTypePersonalDetails.html), [secureValueTypePassport](../constructors/secureValueTypePassport.html), [secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.html), [secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.html), [secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.html), [secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.html), [secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.html), [secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.html), [secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.html), [secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.html)|
|file\_hash|Array of [bytes](/API_docs/types/bytes.html) | Yes|Hash|
|text|[string](/API_docs/types/string.html) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.html)


### Example:

```
$secureValueErrorTranslationFiles = ['_' => 'secureValueErrorTranslationFiles', 'type' => SecureValueType, 'file_hash' => ['bytes', 'bytes'], 'text' => 'string'];
```  
