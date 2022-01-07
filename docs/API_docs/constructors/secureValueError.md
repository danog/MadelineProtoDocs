---
title: "secureValueError"
description: "Secure value error"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueError  
[Back to constructors index](index.md)



Secure value error

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Type of element which has the issue|
|hash|[bytes](../types/bytes.md) | Yes|Hash|
|text|[string](../types/string.md) | Yes|Error message|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueError = ['_' => 'secureValueError', 'type' => SecureValueType, 'hash' => 'bytes', 'text' => 'string'];
```  
