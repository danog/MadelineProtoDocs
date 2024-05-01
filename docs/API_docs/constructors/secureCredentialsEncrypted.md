---
title: "secureCredentialsEncrypted"
description: "Encrypted credentials required to decrypt telegram passport data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureCredentialsEncrypted  
[Back to constructors index](/API_docs/constructors/index.html)



Encrypted credentials required to decrypt [telegram passport](https://core.telegram.org/passport) data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|data|[bytes](/API_docs/types/bytes.html) | Yes|Encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication, as described in [decrypting data »](https://core.telegram.org/passport#decrypting-data)|
|hash|[bytes](/API_docs/types/bytes.html) | Yes|Data hash for data authentication as described in [decrypting data »](https://core.telegram.org/passport#decrypting-data)|
|secret|[bytes](/API_docs/types/bytes.html) | Yes|Secret, encrypted with the bot's public RSA key, required for data decryption as described in [decrypting data »](https://core.telegram.org/passport#decrypting-data)|



### Type: [SecureCredentialsEncrypted](/API_docs/types/SecureCredentialsEncrypted.html)


### Example:

```
$secureCredentialsEncrypted = ['_' => 'secureCredentialsEncrypted', 'data' => 'bytes', 'hash' => 'bytes', 'secret' => 'bytes'];
```  
