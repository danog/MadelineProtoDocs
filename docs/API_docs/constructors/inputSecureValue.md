---
title: "inputSecureValue"
description: "Secure value, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputSecureValue  
[Back to constructors index](/API_docs/constructors/index.html)



Secure value, [for more info see the passport docs »](https://core.telegram.org/passport/encryption#encryption)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.html) | Yes|Secure [passport](https://core.telegram.org/passport) value type|
|data|[SecureData](/API_docs/types/SecureData.html) | Optional|Encrypted [Telegram Passport](https://core.telegram.org/passport) element data|
|front\_side|[InputSecureFile](/API_docs/types/InputSecureFile.html) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with the front side of the document|
|reverse\_side|[InputSecureFile](/API_docs/types/InputSecureFile.html) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with the reverse side of the document|
|selfie|[InputSecureFile](/API_docs/types/InputSecureFile.html) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with a selfie of the user holding the document|
|translation|Array of [InputSecureFile](/API_docs/types/InputSecureFile.html) | Optional|Array of encrypted [passport](https://core.telegram.org/passport) files with translated versions of the provided documents|
|files|Array of [InputSecureFile](/API_docs/types/InputSecureFile.html) | Optional|Array of encrypted [passport](https://core.telegram.org/passport) files with photos the of the documents|
|plain\_data|[SecurePlainData](/API_docs/types/SecurePlainData.html) | Optional|Plaintext verified [passport](https://core.telegram.org/passport) data|



### Type: [InputSecureValue](/API_docs/types/InputSecureValue.html)


### Example:

```
$inputSecureValue = ['_' => 'inputSecureValue', 'type' => SecureValueType, 'data' => SecureData, 'front_side' => InputSecureFile, 'reverse_side' => InputSecureFile, 'selfie' => InputSecureFile, 'translation' => [InputSecureFile, InputSecureFile], 'files' => [InputSecureFile, InputSecureFile], 'plain_data' => SecurePlainData];
```  
