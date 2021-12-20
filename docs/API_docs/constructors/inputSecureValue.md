---
title: "inputSecureValue"
description: "Secure value, for more info see the passport docs »"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureValue  
[Back to constructors index](index.md)



Secure value, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Secure [passport](https://core.telegram.org/passport) value type|
|data|[SecureData](../types/SecureData.md) | Optional|Encrypted [Telegram Passport](https://core.telegram.org/passport) element data|
|front\_side|[InputSecureFile](../types/InputSecureFile.md) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with the front side of the document|
|reverse\_side|[InputSecureFile](../types/InputSecureFile.md) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with the reverse side of the document|
|selfie|[InputSecureFile](../types/InputSecureFile.md) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with a selfie of the user holding the document|
|translation|Array of [InputSecureFile](../types/InputSecureFile.md) | Optional|Array of encrypted [passport](https://core.telegram.org/passport) files with translated versions of the provided documents|
|files|Array of [InputSecureFile](../types/InputSecureFile.md) | Optional|Array of encrypted [passport](https://core.telegram.org/passport) files with photos the of the documents|
|plain\_data|[SecurePlainData](../types/SecurePlainData.md) | Optional|Plaintext verified [passport](https://core.telegram.org/passport) data|



### Type: [InputSecureValue](../types/InputSecureValue.md)


### Example:

```php
$inputSecureValue = ['_' => 'inputSecureValue', 'type' => SecureValueType, 'data' => SecureData, 'front_side' => InputSecureFile, 'reverse_side' => InputSecureFile, 'selfie' => InputSecureFile, 'translation' => [InputSecureFile, InputSecureFile], 'files' => [InputSecureFile, InputSecureFile], 'plain_data' => SecurePlainData];
```  


Or, if you're into Lua:

```lua
inputSecureValue={_='inputSecureValue', type=SecureValueType, data=SecureData, front_side=InputSecureFile, reverse_side=InputSecureFile, selfie=InputSecureFile, translation={InputSecureFile}, files={InputSecureFile}, plain_data=SecurePlainData}

```


