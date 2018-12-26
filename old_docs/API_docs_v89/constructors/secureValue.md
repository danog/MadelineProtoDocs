---
title: secureValue
description: Secure value
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValue  
[Back to constructors index](index.md)



Secure value

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Type|
|data|[SecureData](../types/SecureData.md) | Optional|Data|
|front\_side|[SecureFile](../types/SecureFile.md) | Optional|Front side|
|reverse\_side|[SecureFile](../types/SecureFile.md) | Optional|Reverse side|
|selfie|[SecureFile](../types/SecureFile.md) | Optional|Selfie|
|translation|Array of [SecureFile](../types/SecureFile.md) | Optional|Translation|
|files|Array of [SecureFile](../types/SecureFile.md) | Optional|Files|
|plain\_data|[SecurePlainData](../types/SecurePlainData.md) | Optional|Plain data|
|hash|[bytes](../types/bytes.md) | Yes|Hash|



### Type: [SecureValue](../types/SecureValue.md)


### Example:

```php
$secureValue = ['_' => 'secureValue', 'type' => SecureValueType, 'data' => SecureData, 'front_side' => SecureFile, 'reverse_side' => SecureFile, 'selfie' => SecureFile, 'translation' => [SecureFile, SecureFile], 'files' => [SecureFile, SecureFile], 'plain_data' => SecurePlainData, 'hash' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureValue", "type": SecureValueType, "data": SecureData, "front_side": SecureFile, "reverse_side": SecureFile, "selfie": SecureFile, "translation": [SecureFile], "files": [SecureFile], "plain_data": SecurePlainData, "hash": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
secureValue={_='secureValue', type=SecureValueType, data=SecureData, front_side=SecureFile, reverse_side=SecureFile, selfie=SecureFile, translation={SecureFile}, files={SecureFile}, plain_data=SecurePlainData, hash='bytes'}

```


