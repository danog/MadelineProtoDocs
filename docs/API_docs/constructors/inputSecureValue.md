---
title: inputSecureValue
description: inputSecureValue attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureValue  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|
|data|[SecureData](../types/SecureData.md) | Optional|
|front\_side|[InputSecureFile](../types/InputSecureFile.md) | Optional|
|reverse\_side|[InputSecureFile](../types/InputSecureFile.md) | Optional|
|selfie|[InputSecureFile](../types/InputSecureFile.md) | Optional|
|files|Array of [InputSecureFile](../types/InputSecureFile.md) | Optional|
|plain\_data|[SecurePlainData](../types/SecurePlainData.md) | Optional|



### Type: [InputSecureValue](../types/InputSecureValue.md)


### Example:

```php
$inputSecureValue = ['_' => 'inputSecureValue', 'type' => SecureValueType, 'data' => SecureData, 'front_side' => InputSecureFile, 'reverse_side' => InputSecureFile, 'selfie' => InputSecureFile, 'files' => [InputSecureFile, InputSecureFile], 'plain_data' => SecurePlainData];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputSecureValue", "type": SecureValueType, "data": SecureData, "front_side": InputSecureFile, "reverse_side": InputSecureFile, "selfie": InputSecureFile, "files": [InputSecureFile], "plain_data": SecurePlainData}
```


Or, if you're into Lua:

```lua
inputSecureValue={_='inputSecureValue', type=SecureValueType, data=SecureData, front_side=InputSecureFile, reverse_side=InputSecureFile, selfie=InputSecureFile, files={InputSecureFile}, plain_data=SecurePlainData}

```


