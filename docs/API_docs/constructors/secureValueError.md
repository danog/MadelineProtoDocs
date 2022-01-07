---
title: "secureValueError"
description: "Secure value error"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueError  
[Back to constructors index](/API_docs/constructors/index.md)



Secure value error

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.md) | Yes|Type of element which has the issue|
|hash|[bytes](/API_docs/types/bytes.md) | Yes|Hash|
|text|[string](/API_docs/types/string.md) | Yes|Error message|



### Type: [SecureValueError](/API_docs/types/SecureValueError.md)


### Example:

```php
$secureValueError = ['_' => 'secureValueError', 'type' => SecureValueType, 'hash' => 'bytes', 'text' => 'string'];
```  
