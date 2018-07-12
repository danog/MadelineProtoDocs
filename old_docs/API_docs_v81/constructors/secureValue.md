---
title: secureValue
description: secureValue attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValue  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|
|data|[SecureData](../types/SecureData.md) | Optional|
|front\_side|[SecureFile](../types/SecureFile.md) | Optional|
|reverse\_side|[SecureFile](../types/SecureFile.md) | Optional|
|selfie|[SecureFile](../types/SecureFile.md) | Optional|
|files|Array of [SecureFile](../types/SecureFile.md) | Optional|
|plain\_data|[SecurePlainData](../types/SecurePlainData.md) | Optional|
|hash|[bytes](../types/bytes.md) | Yes|



### Type: [SecureValue](../types/SecureValue.md)


### Example:

```
$secureValue = ['_' => 'secureValue', 'type' => SecureValueType, 'data' => SecureData, 'front_side' => SecureFile, 'reverse_side' => SecureFile, 'selfie' => SecureFile, 'files' => [SecureFile, SecureFile], 'plain_data' => SecurePlainData, 'hash' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValue", "type": SecureValueType, "data": SecureData, "front_side": SecureFile, "reverse_side": SecureFile, "selfie": SecureFile, "files": [SecureFile], "plain_data": SecurePlainData, "hash": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:  


```
secureValue={_='secureValue', type=SecureValueType, data=SecureData, front_side=SecureFile, reverse_side=SecureFile, selfie=SecureFile, files={SecureFile}, plain_data=SecurePlainData, hash='bytes'}

```


