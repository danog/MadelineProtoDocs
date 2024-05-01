---
title: "secureValue"
description: "Secure value"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureValue  
[Back to constructors index](/API_docs/constructors/index.html)



Secure value

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[SecureValueType](/API_docs/types/SecureValueType.html) | Yes|Secure [passport](https://core.telegram.org/passport) value type|
|data|[SecureData](/API_docs/types/SecureData.html) | Optional|Encrypted [Telegram Passport](https://core.telegram.org/passport) element data|
|front\_side|[SecureFile](/API_docs/types/SecureFile.html) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with the front side of the document|
|reverse\_side|[SecureFile](/API_docs/types/SecureFile.html) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with the reverse side of the document|
|selfie|[SecureFile](/API_docs/types/SecureFile.html) | Optional|Encrypted [passport](https://core.telegram.org/passport) file with a selfie of the user holding the document|
|translation|Array of [SecureFile](/API_docs/types/SecureFile.html) | Optional|Array of encrypted [passport](https://core.telegram.org/passport) files with translated versions of the provided documents|
|files|Array of [SecureFile](/API_docs/types/SecureFile.html) | Optional|Array of encrypted [passport](https://core.telegram.org/passport) files with photos the of the documents|
|plain\_data|[SecurePlainData](/API_docs/types/SecurePlainData.html) | Optional|Plaintext verified [passport](https://core.telegram.org/passport) data|
|hash|[bytes](/API_docs/types/bytes.html) | Yes|Data hash|



### Type: [SecureValue](/API_docs/types/SecureValue.html)


### Example:

```
$secureValue = ['_' => 'secureValue', 'type' => SecureValueType, 'data' => SecureData, 'front_side' => SecureFile, 'reverse_side' => SecureFile, 'selfie' => SecureFile, 'translation' => [SecureFile, SecureFile], 'files' => [SecureFile, SecureFile], 'plain_data' => SecurePlainData, 'hash' => 'bytes'];
```  
