---
title: securePasswordKdfAlgoSHA512
description: Secure password kdf algo sha512
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: securePasswordKdfAlgoSHA512  
[Back to constructors index](index.md)



Secure password kdf algo sha512

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|salt|[bytes](../types/bytes.md) | Yes|Salt|



### Type: [SecurePasswordKdfAlgo](../types/SecurePasswordKdfAlgo.md)


### Example:

```php
$securePasswordKdfAlgoSHA512 = ['_' => 'securePasswordKdfAlgoSHA512', 'salt' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "securePasswordKdfAlgoSHA512", "salt": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
securePasswordKdfAlgoSHA512={_='securePasswordKdfAlgoSHA512', salt='bytes'}

```


