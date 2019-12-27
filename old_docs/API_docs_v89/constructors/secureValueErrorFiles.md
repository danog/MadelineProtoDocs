---
title: secureValueErrorFiles
description: Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorFiles  
[Back to constructors index](index.md)



Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|One of [secureValueTypeUtilityBill](../constructors/secureValueTypeUtilityBill.md), [secureValueTypeBankStatement](../constructors/secureValueTypeBankStatement.md), [secureValueTypeRentalAgreement](../constructors/secureValueTypeRentalAgreement.md), [secureValueTypePassportRegistration](../constructors/secureValueTypePassportRegistration.md), [secureValueTypeTemporaryRegistration](../constructors/secureValueTypeTemporaryRegistration.md)|
|file\_hash|Array of [bytes](../types/bytes.md) | Yes|File hash|
|text|[string](../types/string.md) | Yes|Error message|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueErrorFiles = ['_' => 'secureValueErrorFiles', 'type' => SecureValueType, 'file_hash' => ['bytes', 'bytes'], 'text' => 'string'];
```  


Or, if you're into Lua:

```lua
secureValueErrorFiles={_='secureValueErrorFiles', type=SecureValueType, file_hash={'bytes'}, text='string'}

```


