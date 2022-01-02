---
title: "secureValue"
description: "Secure value"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValue  
[Back to constructors index](index.md)



Secure value

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](../types/SecureValueType.md) | Yes|Secure [passport](https://core.telegram.org/passport) value type|
|data|[SecureData](../types/SecureData.md) | Optional|Encrypted [Telegram Passport](https://core.telegram.org/passport) element data|
|front\_side|[SecureFile](../types/SecureFile.md) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with the front side of the document|
|reverse\_side|[SecureFile](../types/SecureFile.md) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with the reverse side of the document|
|selfie|[SecureFile](../types/SecureFile.md) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with a selfie of the user holding the document|
|translation|Array of [SecureFile](../types/SecureFile.md) | Optional|Array of encrypted [passport](https://core.telegram.org/passport) files with translated versions of the provided documents|
|files|Array of [SecureFile](../types/SecureFile.md) | Optional|Array of encrypted [passport](https://core.telegram.org/passport) files with photos the of the documents|
|plain\_data|[SecurePlainData](../types/SecurePlainData.md) | Optional|Plaintext verified [passport](https://core.telegram.org/passport) data|
|hash|[bytes](../types/bytes.md) | Yes|Data hash|



### Type: [SecureValue](../types/SecureValue.md)


### Example:

```php
$secureValue = ['_' => 'secureValue', 'type' => SecureValueType, 'data' => SecureData, 'front_side' => SecureFile, 'reverse_side' => SecureFile, 'selfie' => SecureFile, 'translation' => [SecureFile, SecureFile], 'files' => [SecureFile, SecureFile], 'plain_data' => SecurePlainData, 'hash' => 'bytes'];
```  


Or, if you're into Lua:

```lua
secureValue={_='secureValue', type=SecureValueType, data=SecureData, front_side=SecureFile, reverse_side=SecureFile, selfie=SecureFile, translation={SecureFile}, files={SecureFile}, plain_data=SecurePlainData, hash='bytes'}

```


