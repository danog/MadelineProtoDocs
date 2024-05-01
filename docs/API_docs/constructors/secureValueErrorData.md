---
title: "secureValueErrorData"
description: "Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorData  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.html) | Yes|The section of the user's Telegram Passport which has the error, one of [secureValueTypePersonalDetails](../constructors/secureValueTypePersonalDetails.html), [secureValueTypePassport](../constructors/secureValueTypePassport.html), [secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.html), [secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.html), [secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.html), [secureValueTypeAddress](../constructors/secureValueTypeAddress.html)|
|data\_hash|[bytes](/API_docs/types/bytes.html) | Yes|Data hash|
|field|[string](/API_docs/types/string.html) | Yes|Name of the data field which has the error|
|text|[string](/API_docs/types/string.html) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.html)


### Example:

```
$secureValueErrorData = ['_' => 'secureValueErrorData', 'type' => SecureValueType, 'data_hash' => 'bytes', 'field' => 'string', 'text' => 'string'];
```  
