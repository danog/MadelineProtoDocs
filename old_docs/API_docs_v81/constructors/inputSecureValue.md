---
title: inputSecureValue
description: Secure value
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureValue  
[Back to constructors index](index.md)



Secure value

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Type|
|data|[SecureData](../types/SecureData.md) | Optional|Data|
|front\_side|[InputSecureFile](../types/InputSecureFile.md) | Optional|Front side|
|reverse\_side|[InputSecureFile](../types/InputSecureFile.md) | Optional|Reverse side|
|selfie|[InputSecureFile](../types/InputSecureFile.md) | Optional|Selfie|
|files|Array of [InputSecureFile](../types/InputSecureFile.md) | Optional|Files|
|plain\_data|[SecurePlainData](../types/SecurePlainData.md) | Optional|Plain data|



### Type: [InputSecureValue](../types/InputSecureValue.md)


### Example:

```php
$inputSecureValue = ['_' => 'inputSecureValue', 'type' => SecureValueType, 'data' => SecureData, 'front_side' => InputSecureFile, 'reverse_side' => InputSecureFile, 'selfie' => InputSecureFile, 'files' => [InputSecureFile, InputSecureFile], 'plain_data' => SecurePlainData];
```  


Or, if you're into Lua:

```lua
inputSecureValue={_='inputSecureValue', type=SecureValueType, data=SecureData, front_side=InputSecureFile, reverse_side=InputSecureFile, selfie=InputSecureFile, files={InputSecureFile}, plain_data=SecurePlainData}

```


