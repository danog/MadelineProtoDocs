---
title: passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow
description: Password kdf algo sha256sha256pbkdf2hmacsh a512iter100000 sha256 mod pow
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow  
[Back to constructors index](index.md)



Password kdf algo sha256sha256pbkdf2hmacsh a512iter100000 sha256 mod pow

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|salt1|[bytes](../types/bytes.md) | Yes|Salt1|
|salt2|[bytes](../types/bytes.md) | Yes|Salt2|
|g|[int](../types/int.md) | Yes|G|
|p|[bytes](../types/bytes.md) | Yes|P|



### Type: [PasswordKdfAlgo](../types/PasswordKdfAlgo.md)


### Example:

```php
$passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow = ['_' => 'passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow', 'salt1' => 'bytes', 'salt2' => 'bytes', 'g' => int, 'p' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow", "salt1": {"_": "bytes", "bytes":"base64 encoded bytes"}, "salt2": {"_": "bytes", "bytes":"base64 encoded bytes"}, "g": int, "p": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow={_='passwordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow', salt1='bytes', salt2='bytes', g=int, p='bytes'}

```


