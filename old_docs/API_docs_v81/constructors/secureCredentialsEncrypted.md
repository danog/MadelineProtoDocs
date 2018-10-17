---
title: secureCredentialsEncrypted
description: secureCredentialsEncrypted attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureCredentialsEncrypted  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|data|[bytes](../types/bytes.md) | Yes|
|hash|[bytes](../types/bytes.md) | Yes|
|secret|[bytes](../types/bytes.md) | Yes|



### Type: [SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md)


### Example:

```php
$secureCredentialsEncrypted = ['_' => 'secureCredentialsEncrypted', 'data' => 'bytes', 'hash' => 'bytes', 'secret' => 'bytes'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "secureCredentialsEncrypted", "data": {"_": "bytes", "bytes":"base64 encoded bytes"}, "hash": {"_": "bytes", "bytes":"base64 encoded bytes"}, "secret": {"_": "bytes", "bytes":"base64 encoded bytes"}}
```


Or, if you're into Lua:

```lua
secureCredentialsEncrypted={_='secureCredentialsEncrypted', data='bytes', hash='bytes', secret='bytes'}

```


