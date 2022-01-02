---
title: "secureData"
description: "Secure passport data, for more info see the passport docs »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: secureData  
[Back to constructors index](index.md)



Secure [passport](https://core.telegram.org/passport) data, for more info [see the passport docs »](https://core.telegram.org/passport/encryption#securedata)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|data|[bytes](../types/bytes.md) | Yes|Data|
|data\_hash|[bytes](../types/bytes.md) | Yes|Data hash|
|secret|[bytes](../types/bytes.md) | Yes|Secret|



### Type: [SecureData](../types/SecureData.md)


### Example:

```php
$secureData = ['_' => 'secureData', 'data' => 'bytes', 'data_hash' => 'bytes', 'secret' => 'bytes'];
```  


Or, if you're into Lua:

```lua
secureData={_='secureData', data='bytes', data_hash='bytes', secret='bytes'}

```


