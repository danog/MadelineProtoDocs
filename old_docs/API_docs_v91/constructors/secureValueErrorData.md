---
title: secureValueErrorData
description: Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorData  
[Back to constructors index](index.md)



Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|The section of the user's Telegram Passport which has the error, one of [secureValueTypePersonalDetails](../constructors/secureValueTypePersonalDetails.md), [secureValueTypePassport](../constructors/secureValueTypePassport.md), [secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.md), [secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.md), [secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.md), [secureValueTypeAddress](../constructors/secureValueTypeAddress.md)|
|data\_hash|[bytes](../types/bytes.md) | Yes|Data hash|
|field|[string](../types/string.md) | Yes|Name of the data field which has the error|
|text|[string](../types/string.md) | Yes|Error message|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueErrorData = ['_' => 'secureValueErrorData', 'type' => SecureValueType, 'data_hash' => 'bytes', 'field' => 'string', 'text' => 'string'];
```  


Or, if you're into Lua:

```lua
secureValueErrorData={_='secureValueErrorData', type=SecureValueType, data_hash='bytes', field='string', text='string'}

```


