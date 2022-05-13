---
title: "passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow"
description: "This key derivation algorithm defines that SRP 2FA login must be used"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow  
[Back to constructors index](/API_docs/constructors/index.html)



This key derivation algorithm defines that [SRP 2FA login](https://core.telegram.org/api/srp) must be used

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|salt1|[bytes](/API_docs/types/bytes.html) | Yes|One of two salts used by the derivation function (see [SRP 2FA login](https://core.telegram.org/api/srp))|
|salt2|[bytes](/API_docs/types/bytes.html) | Yes|One of two salts used by the derivation function (see [SRP 2FA login](https://core.telegram.org/api/srp))|
|g|[int](/API_docs/types/int.html) | Yes|Base (see [SRP 2FA login](https://core.telegram.org/api/srp))|
|p|[bytes](/API_docs/types/bytes.html) | Yes|2048-bit modulus (see [SRP 2FA login](https://core.telegram.org/api/srp))|



### Type: [PasswordKdfAlgo](/API_docs/types/PasswordKdfAlgo.html)


### Example:

```
$passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow = ['_' => 'passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow', 'salt1' => 'bytes', 'salt2' => 'bytes', 'g' => int, 'p' => 'bytes'];
```  
