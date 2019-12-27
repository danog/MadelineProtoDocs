---
title: passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow
description: This key derivation algorithm defines that [SRP 2FA login](https://core.telegram.org/api/srp) must be used
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow  
[Back to constructors index](index.md)



This key derivation algorithm defines that [SRP 2FA login](https://core.telegram.org/api/srp) must be used

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|salt1|[bytes](../types/bytes.md) | Yes|One of two salts used by the derivation function (see [SRP 2FA login](https://core.telegram.org/api/srp))|
|salt2|[bytes](../types/bytes.md) | Yes|One of two salts used by the derivation function (see [SRP 2FA login](https://core.telegram.org/api/srp))|
|g|[int](../types/int.md) | Yes|Base (see [SRP 2FA login](https://core.telegram.org/api/srp))|
|p|[bytes](../types/bytes.md) | Yes|2048-bit modulus (see [SRP 2FA login](https://core.telegram.org/api/srp))|



### Type: [PasswordKdfAlgo](../types/PasswordKdfAlgo.md)


### Example:

```php
$passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow = ['_' => 'passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow', 'salt1' => 'bytes', 'salt2' => 'bytes', 'g' => int, 'p' => 'bytes'];
```  


Or, if you're into Lua:

```lua
passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow={_='passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow', salt1='bytes', salt2='bytes', g=int, p='bytes'}

```


