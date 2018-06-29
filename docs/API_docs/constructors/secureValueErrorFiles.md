---
title: secureValueErrorFiles
description: secureValueErrorFiles attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValueErrorFiles  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|
|file\_hash|Array of [bytes](../types/bytes.md) | Yes|
|text|[string](../types/string.md) | Yes|



### Type: [SecureValueError](../types/SecureValueError.md)


### Example:

```
$secureValueErrorFiles = ['_' => 'secureValueErrorFiles', 'type' => SecureValueType, 'file_hash' => ['bytes', 'bytes'], 'text' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValueErrorFiles", "type": SecureValueType, "file_hash": [{"_": "bytes", "bytes":"base64 encoded bytes"}], "text": "string"}
```


Or, if you're into Lua:  


```
secureValueErrorFiles={_='secureValueErrorFiles', type=SecureValueType, file_hash={'bytes'}, text='string'}

```


