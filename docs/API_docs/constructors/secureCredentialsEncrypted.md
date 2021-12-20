---
title: "secureCredentialsEncrypted"
description: "Encrypted credentials required to decrypt telegram passport data."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureCredentialsEncrypted  
[Back to constructors index](index.md)



Encrypted credentials required to decrypt [telegram passport](https://core.telegram.org/passport) data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|data|[bytes](../types/bytes.md) | Yes|Encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication, as described in [decrypting data »](https://core.telegram.org/passport#decrypting-data)|
|hash|[bytes](../types/bytes.md) | Yes|Data hash for data authentication as described in [decrypting data »](https://core.telegram.org/passport#decrypting-data)|
|secret|[bytes](../types/bytes.md) | Yes|Secret, encrypted with the bot's public RSA key, required for data decryption as described in [decrypting data »](https://core.telegram.org/passport#decrypting-data)|



### Type: [SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md)


### Example:

```php
$secureCredentialsEncrypted = ['_' => 'secureCredentialsEncrypted', 'data' => 'bytes', 'hash' => 'bytes', 'secret' => 'bytes'];
```  


Or, if you're into Lua:

```lua
secureCredentialsEncrypted={_='secureCredentialsEncrypted', data='bytes', hash='bytes', secret='bytes'}

```


