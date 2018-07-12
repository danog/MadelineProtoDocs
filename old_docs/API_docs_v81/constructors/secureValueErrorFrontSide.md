---
title: secureValueErrorFrontSide
description: secureValueErrorFrontSide attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorFrontSide  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|
|file\_hash|[bytes](../types/bytes.md) | Yes|
|text|[string](../types/string.md) | Yes|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```
$secureValueErrorFrontSide = ['_' => 'secureValueErrorFrontSide', 'type' => SecureValueType, 'file_hash' => 'bytes', 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValueErrorFrontSide", "type": SecureValueType, "file_hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "text": "string"}
```


Or, if you're into Lua:  


```
secureValueErrorFrontSide={_='secureValueErrorFrontSide', type=SecureValueType, file_hash='bytes', text='string'}

```


