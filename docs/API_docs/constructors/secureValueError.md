---
title: "secureValueError"
description: "Secure value error"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueError  
[Back to constructors index](/API_docs/constructors/index.html)



Secure value error

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.html) | Yes|Type of element which has the issue|
|hash|[bytes](/API_docs/types/bytes.html) | Yes|Hash|
|text|[string](/API_docs/types/string.html) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.html)


### Example:

```
$secureValueError = ['_' => 'secureValueError', 'type' => SecureValueType, 'hash' => 'bytes', 'text' => 'string'];
```  
