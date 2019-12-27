---
title: secureValueErrorTranslationFile
description: Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorTranslationFile  
[Back to constructors index](index.md)



Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|One of [secureValueTypePersonalDetails](../constructors/secureValueTypePersonalDetails.md), [secureValueTypePassport](../constructors/secureValueTypePassport.md), [secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.md), [secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.md), [secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.md), [secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.md), [secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.md), [secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.md), [secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.md), [secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.md)|
|file\_hash|[bytes](../types/bytes.md) | Yes|File hash|
|text|[string](../types/string.md) | Yes|Error message|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueErrorTranslationFile = ['_' => 'secureValueErrorTranslationFile', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  


Or, if you're into Lua:

```lua
secureValueErrorTranslationFile={_='secureValueErrorTranslationFile', type=SecureValueType, file_hash='bytes', text='string'}

```


