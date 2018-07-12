---
title: secureValueErrorData
description: secureValueErrorData attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorData  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|
|data\_hash|[bytes](../types/bytes.md) | Yes|
|field|[string](../types/string.md) | Yes|
|text|[string](../types/string.md) | Yes|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```
$secureValueErrorData = ['_' => 'secureValueErrorData', 'type' => SecureValueType, 'data_hash' => 'bytes', 'field' => 'string', 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValueErrorData", "type": SecureValueType, "data_hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "field": "string", "text": "string"}
```


Or, if you're into Lua:  


```
secureValueErrorData={_='secureValueErrorData', type=SecureValueType, data_hash='bytes', field='string', text='string'}

```


