---
title: secureValueErrorFrontSide
description: Secure value error front side
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorFrontSide  
[Back to constructors index](index.md)



Secure value error front side

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Type|
|file\_hash|[bytes](../types/bytes.md) | Yes|File hash|
|text|[string](../types/string.md) | Yes|Text|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```php
$secureValueErrorFrontSide = ['_' => 'secureValueErrorFrontSide', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValueErrorFrontSide", "type": SecureValueType, "file_hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "text": "string"}
```


Or, if you're into Lua:

```lua
secureValueErrorFrontSide={_='secureValueErrorFrontSide', type=SecureValueType, file_hash='bytes', text='string'}

```


