---
title: "secureValueErrorSelfie"
description: "Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorSelfie  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.html) | Yes|One of [secureValueTypePassport](../constructors/secureValueTypePassport.html), [secureValueTypeDriverLicense](../constructors/secureValueTypeDriverLicense.html), [secureValueTypeIdentityCard](../constructors/secureValueTypeIdentityCard.html), [secureValueTypeInternalPassport](../constructors/secureValueTypeInternalPassport.html)|
|file\_hash|[bytes](/API_docs/types/bytes.html) | Yes|File hash|
|text|[string](/API_docs/types/string.html) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.html)


### Example:

```
$secureValueErrorSelfie = ['_' => 'secureValueErrorSelfie', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  
