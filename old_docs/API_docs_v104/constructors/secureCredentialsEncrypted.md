---
title: secureCredentialsEncrypted
description: Secure credentials encrypted
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureCredentialsEncrypted  
[Back to constructors index](index.md)



Secure credentials encrypted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|data|[bytes](../types/bytes.md) | Yes|Data|
|hash|[bytes](../types/bytes.md) | Yes|Hash|
|secret|[bytes](../types/bytes.md) | Yes|Secret|



### Type: [SecureCredentialsEncrypted](../types/SecureCredentialsEncrypted.md)


### Example:

```php
$secureCredentialsEncrypted = ['_' => 'secureCredentialsEncrypted', 'data' => 'bytes', 'hash' => 'bytes', 'secret' => 'bytes'];
```  


Or, if you're into Lua:

```lua
secureCredentialsEncrypted={_='secureCredentialsEncrypted', data='bytes', hash='bytes', secret='bytes'}

```


