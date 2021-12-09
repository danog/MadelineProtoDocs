---
title: secureValueErrorTranslationFiles
description: Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation changes.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorTranslationFiles  
[Back to constructors index](index.md)



Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|One of [secureValueTypePersonalDetails](../constructors/secureValueTypePersonalDetails.md), [secureValueTypePassport](../constructors/secureValueTypePassport.md), [secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.md), [secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.md), [secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.md), [secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.md), [secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.md), [secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.md), [secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.md), [secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.md)|
|file\_hash|Array of [bytes](../types/bytes.md) | Yes|Hash|
|text|[string](../types/string.md) | Yes|Error message|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueErrorTranslationFiles = ['_' => 'secureValueErrorTranslationFiles', 'type' => SecureValueType, 'file_hash' => ['bytes', 'bytes'], 'text' => 'string'];
```  


Or, if you're into Lua:

```lua
secureValueErrorTranslationFiles={_='secureValueErrorTranslationFiles', type=SecureValueType, file_hash={'bytes'}, text='string'}

```


